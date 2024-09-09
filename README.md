

---

Coffee Shop

            Project Overview

The Coffee Shop project is a Python application that simulates a coffee shop system with a focus on Object-Oriented Programming (OOP) principles. It involves three main entities: `Customer`, `Coffee`, and `Order`, and demonstrates their interactions within the system. 

                Classes

- Customer: Manages customer details and their orders. Includes methods for creating orders and determining the most valuable customer for a specific coffee.
- Coffee: Manages coffee details and related orders. Provides methods to compute the total number of orders and the average price of orders.
- Order: Represents an order made by a customer for a specific coffee, including the price of the order.

  Features

- Customer:
  - Create and manage orders.
  - Retrieve all orders and coffees ordered by the customer.
  - Determine the customer who has spent the most on a specific coffee.

- Coffee:
  - Track orders and customers who ordered the coffee.
  - Calculate the number of orders and average price of orders.

- Order:
  - Link a customer with a coffee and track the order's price.


   
         Usage

         Running Tests

To ensure everything is working correctly, run the test suite using `unittest`:

```bash
python -m unittest discover tests/
```




```

 Testing

- Unit Tests: The project includes unit tests to verify the functionality of each class. Tests are located in the `tests/` directory and can be run using the command:

  bash
  python -m unittest discover tests/
  ```

 Contributing

Contributions to this project are welcome. If you have suggestions or improvements, please follow these steps:


 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

        Acknowledgements

- Inspired by common practices in Object-Oriented Programming.
- Python documentation for guidelines and best practices.

