#!/usr/bin/env python3
"""
Project Island - Total Drama style contestant generator
Generates contestants with name, age, gender.

Usage: python generator.py --count 10 --seed 42 --output outputs/contestants.json
"""
import json
import random
import argparse
import os

def load_data():
    base_dir = os.path.join(os.path.dirname(__file__), "data")
    with open(os.path.join(base_dir, "names.json"), "r", encoding="utf-8") as f:
        names = json.load(f)
    with open(os.path.join(base_dir, "surnames.json"), "r", encoding="utf-8") as f:
        surnames = json.load(f)
    return names, surnames

def random_name(names, surnames, gender):
    if gender == "male":
        pool = names.get("male") or names.get("neutral") or []
    elif gender == "female":
        pool = names.get("female") or names.get("neutral") or []
    else:
        pool = (names.get("neutral", []) + names.get("male", []) + names.get("female", []))
    if not pool:
        pool = ["Alex"]
    first = random.choice(pool)
    last = random.choice(surnames) if surnames else "Doe"
    return f"{first} {last}"

def random_gender():
    return random.choice(["male", "female", "non-binary"])

def random_age():
    # Total Drama-style contestants are typically teens/young adults
    return random.randint(16, 28)

def generate(count=8, specified_genders=None):
    names, surnames = load_data()
    contestants = []
    for i in range(count):
        if specified_genders and i < len(specified_genders):
            gender = specified_genders[i]
        else:
            gender = random_gender()
        contestant = {
            "id": i + 1,
            "name": random_name(names, surnames, gender),
            "age": random_age(),
            "gender": gender,
            "bio": "",
        }
        contestants.append(contestant)
    return contestants

def main():
    parser = argparse.ArgumentParser(description="Project Island - Contestant generator")
    parser.add_argument("--count", "-c", type=int, default=8, help="Number of contestants to generate")
    parser.add_argument("--seed", "-s", type=int, default=None, help="Random seed")
    parser.add_argument("--output", "-o", type=str, default="outputs/contestants.json", help="Output file")
    parser.add_argument("--genders", "-g", type=str, help="Comma-separated genders to assign in order (male,female,non-binary)")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    specified_genders = None
    if args.genders:
        specified_genders = [g.strip().lower() for g in args.genders.split(",")]

    contestants = generate(args.count, specified_genders)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(contestants, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(contestants)} contestants to {args.output}")


if __name__ == "__main__":
    main()
