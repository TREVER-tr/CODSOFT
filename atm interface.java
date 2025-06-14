import java.util.Scanner;

class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("✅ Deposit successful! Current Balance: $" + balance);
        } else {
            System.out.println("❌ Invalid deposit amount.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("✅ Withdrawal successful! Current Balance: $" + balance);
        } else if (amount > balance) {
            System.out.println("❌ Insufficient balance.");
        } else {
            System.out.println("❌ Invalid withdrawal amount.");
        }
    }
}

class ATM {
    private BankAccount account;

    public ATM(BankAccount account) {
        this.account = account;
    }

    public void showMenu() {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n🌟 ATM Menu 🌟");
            System.out.println("1️⃣ Check Balance");
            System.out.println("2️⃣ Deposit Money");
            System.out.println("3️⃣ Withdraw Money");
            System.out.println("4️⃣ Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("💰 Current Balance: $" + account.getBalance());
                    break;
                case 2:
                    System.out.print("Enter deposit amount: ");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 3:
                    System.out.print("Enter withdrawal amount: ");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 4:
                    System.out.println("🚪 Exiting ATM. Have a great day!");
                    break;
                default:
                    System.out.println("❌ Invalid choice. Please try again.");
            }
        } while (choice != 4);

        scanner.close();
    }
}

public class ATMSystem {
    public static void main(String[] args) {
        BankAccount userAccount = new BankAccount(500);  // Initialize account with $500 balance
        ATM atm = new ATM(userAccount);
        atm.showMenu();
    }
}

