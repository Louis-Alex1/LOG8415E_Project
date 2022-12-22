#!/bin/bash
echo "-Start benchmarking with Sysbench-"

#Read the IP Address of the machine to benchmark
echo "Enter the Ip Address: "
read ipAddress

#Prepare the records for the benchmarking
sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-host=$ipAddress --mysql-user=benchmark --mysql-password=admin123 prepare

#Run the benchmarking
sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-host=$ipAddress --threads=6 --time=60 --mysql-user=benchmark --mysql-password=admin123 run