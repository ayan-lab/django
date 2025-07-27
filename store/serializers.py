from rest_framework import serializers
from .models import Product, Collection, Customer, Order,OrderItem, ProductImage, Cart, CartItem
from decimal import Decimal
from django.db.models.aggregates import Count
from django.db import transaction



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']
    
    product_count = serializers.IntegerField(read_only=True)
    
    
    
    
class CustomerSerializer(serializers.ModelSerializer):
    user_id  = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'phone', 'birth_date', 'user_id', 'membership']
    
    
# class ProductImageSerializer(serializers.ModelSerializer):
    
#     def create(self, validated_data):
#         product_id = self.context['product_id']
#         return ProductImage.objects.create(product_id=product_id, **validated_data)
    
#     class Meta:
#         model = ProductImage
#         fields = ['id','image']
    
    
class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(method_name='get_image_url')

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'image_url']
        
        
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','title','unit_price','price_with_tax','slug','inventory', 'description', 'collection', 'images']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
   
    
    
    # serialize a relationship
    
    #option 1
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all()
    # )
    
    #option 2
    # collection = serializers.StringRelatedField()
    
    #option 3
    # collection = CollectionSerializer()
    
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.8)
    
    
    
    

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','title','unit_price']
   
   
        

        
class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price
    
    class Meta:
        model = CartItem
        fields = ['id','product','quantity', 'total_price']


        

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        #list comprehension
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])

        
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']



 
class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    
    
    # validate teh product id
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Product id not valid')
        return value
    
    
    def save(self, **kwargs):
        product_id = self.validated_data['product_id']
        cart_id = self.context['cart_id']
        quantity = self.validated_data['quantity']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        
        return self.instance
    

    
    class Meta:
        model = CartItem
        fields = ['id','product_id', 'quantity']
        
        
        
        
class UpdateItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = CartItem
       fields = ['quantity']
       
       
class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id','unit_price','product','quantity']       

       
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id','customer','placed_at','payment_status', 'items']
        
        
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']
        
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart exists with id ... ')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError("This cart is empty ...")
        return cart_id
    
    
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']

            customer = Customer.objects.get(user_id=self.context['user_id'])
            order = Order.objects.create(customer=customer)

            cart_items = CartItem.objects.select_related('product').filter(cart_id=cart_id)

            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    unit_price=item.product.unit_price,
                    quantity=item.quantity
                )
                for item in cart_items
            ]

            OrderItem.objects.bulk_create(order_items)
            Cart.objects.filter(pk=cart_id).delete()
            return order
        