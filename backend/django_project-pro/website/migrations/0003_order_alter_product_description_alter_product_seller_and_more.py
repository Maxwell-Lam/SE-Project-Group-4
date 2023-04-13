# Generated by Django 4.1.6 on 2023-04-13 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.shoppingcart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]
