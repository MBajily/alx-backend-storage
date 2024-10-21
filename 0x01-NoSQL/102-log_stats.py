#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from collections import Counter
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    nginx_collection = client.logs.nginx

    # Number of logs
    print(f"{nginx_collection.count_documents({})} logs")

    # Methods and their counts
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_check_count = nginx_collection.count_documents(
                            {"method": "GET", "path": "/status"}
                         )
    print(f"{status_check_count} status check")

    # Top 10 IPs
    print("IPs:")
    ip_counts = Counter(doc["ip"] for doc in nginx_collection.find({},{"ip": 1}))
    for ip, count in ip_counts.most_common(10):
        print(f"\t{ip}: {count}")
