import argparse
from core.bank import bank

def main(num_customers: int):
    b = bank.InitBank()
    b.startSpawningCustomers(num_customers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the bank simulation."
    )
    parser.add_argument(
        "-n", "--num-customers",
        type=int,
        default=1,
        help="Number of customers to spawn"
    )
    args = parser.parse_args()

    main(args.num_customers)