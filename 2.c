#include <stdio.h>

int main() {
    int num1, num2;
    int sum, difference, product, quotient;

    // Input two numbers
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    // Perform arithmetic operations
    sum = num1 + num2;
    difference = num1 - num2;
    product = num1 * num2;
    quotient = num1 / num2;

    // Display the results
    printf("Addition: %.2f\n", sum);
    printf("Subtraction: %.2f\n", difference);
    printf("Multiplication: %.2f\n", product);
    printf("Division: %.2f\n", quotient);

    return 0;
}