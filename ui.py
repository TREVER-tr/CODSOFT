#E-commerece website
import 'package:flutter/material.dart';

void main() {
  runApp(ECommerceApp());
}

class ECommerceApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: ProductScreen(),
    );
  }
}

class ProductScreen extends StatelessWidget {
  final List<Map<String, String>> products = [
    {"name": "Laptop", "price": "\$1200", "image": "assets/laptop.png"},
    {"name": "Smartphone", "price": "\$800", "image": "assets/phone.png"},
    {"name": "Headphones", "price": "\$150", "image": "assets/headphones.png"},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("E-Commerce Store")),
      body: ListView.builder(
        itemCount: products.length,
        itemBuilder: (context, index) {
          return Card(
            margin: EdgeInsets.all(10),
            child: ListTile(
              leading: Image.asset(products[index]["image"]!),
              title: Text(products[index]["name"]!),
              subtitle: Text(products[index]["price"]!),
              trailing: ElevatedButton(
                onPressed: () {},
                child: Text("Buy Now"),
              ),
            ),
          );
        },
      ),
    );
  }
}
#resturant menu
import 'package:flutter/material.dart';

void main() {
  runApp(RestaurantMenuApp());
}

class RestaurantMenuApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MenuScreen(),
    );
  }
}

class MenuScreen extends StatelessWidget {
  final List<Map<String, String>> menuItems = [
    {"name": "Cheese Pizza", "price": "\$10", "image": "assets/pizza.png"},
    {"name": "Burger", "price": "\$8", "image": "assets/burger.png"},
    {"name": "Pasta", "price": "\$12", "image": "assets/pasta.png"},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Restaurant Menu")),
      body: ListView.builder(
        itemCount: menuItems.length,
        itemBuilder: (context, index) {
          return Card(
            margin: EdgeInsets.all(10),
            child: ListTile(
              leading: Image.asset(menuItems[index]["image"]!),
              title: Text(menuItems[index]["name"]!),
              subtitle: Text(menuItems[index]["price"]!),
              trailing: ElevatedButton(
                onPressed: () {},
                child: Text("Order"),
              ),
            ),
          );
        },
      ),
    );
  }
}
# email template
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f5f5f5; }
        .email-container { max-width: 600px; margin: auto; background: #ffffff; padding: 20px; border-radius: 8px; }
        .header { text-align: center; background: #007bff; color: white; padding: 10px; font-size: 20px; }
        .content { padding: 20px; text-align: center; }
        .cta-button { display: inline-block; background: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
        .footer { text-align: center; color: #777; font-size: 12px; padding: 10px; }
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h2>Welcome to Our Service!</h2>
        </div>
        <div class="content">
            <p>Thank you for signing up. We’re excited to have you on board.</p>
            <p>Click below to get started:</p>
            <a href="#" class="cta-button">Start Now</a>
        </div>
        <div class="footer">
            <p>&copy; 2025 Your Company. All Rights Reserved.</p>
        </div>
    </div>
</body>
</html>
# mobile app signup flow
import 'package:flutter/material.dart';

void main() {
  runApp(SignupApp());
}

class SignupApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SignupScreen(),
    );
  }
}

class SignupScreen extends StatefulWidget {
  @override
  _SignupScreenState createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  final _formKey = GlobalKey<FormState>();
  String email = '';
  String password = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Sign Up")),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: "Email"),
                validator: (value) {
                  if (value == null || !value.contains("@")) {
                    return "Enter a valid email";
                  }
                  return null;
                },
                onChanged: (value) => email = value,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: "Password"),
                obscureText: true,
                validator: (value) {
                  if (value == null || value.length < 6) {
                    return "Password must be at least 6 characters";
                  }
                  return null;
                },
                onChanged: (value) => password = value,
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                      content: Text("Signed up successfully!"),
                    ));
                  }
                },
                child: Text("Sign Up"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}



