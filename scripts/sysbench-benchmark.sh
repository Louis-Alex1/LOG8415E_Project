#!/bin/bash
echo "-Start benchmarking with Sysbench-"

echo "Enter the Ip Adress: "
read ipAddress

sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-host=$ipAddress --mysql-user=benchmark --mysql-password=admin123 prepare

sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-host=$ipAddress --threads=6 --time=60 --mysql-user=benchmark --mysql-password=admin123 run