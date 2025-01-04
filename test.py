# from pymongo import MongoClient
# from mongogettersetter import MongoGetterSetter
# from src.LightHouseReport import LightHouseReport
# # Connect to the MongoDB database and collection

# # client = MongoClient("mongodb+srv://sridhardcse:sridhar@cluster0.59wpv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# # db = client["sample_mflix"]
# # collection = db["movies"]



# import json

# with open('LighthouseReport_2024-12-25.report.json', encoding='utf-8') as file:
#     data = json.load(file)

# lhr = LightHouseReport(data)

# print(lhr.is_https)


import logging
from datetime import datetime


logging.basicConfig(
    filename='admin_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def log_action(admin_user, action, details=""):
    log_message = f"Admin: {admin_user}, Action: {action}, Details: {details}"
    logging.info(log_message)
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')

"""
if user:
    session['username']
    session['user_id']
    session['logged_time_stamp']
    session['roles']
    session['language']
    session['cart'] = {'item1': 2, 'item2': 1}.
    session['is_available_tokens']
    session['is_subscribed']





    Monitoring the logs and metrics of large-scale servers is crucial to maintaining performance, ensuring uptime, and identifying issues. When managing a large server, there are several key metrics and logs you should monitor. Below is a comprehensive list of important metrics to track for logging and performance monitoring:

### **1. System Performance Metrics**
- **CPU Utilization**
  - Monitor the overall CPU usage, including per-core usage.
  - Track trends in CPU utilization to spot bottlenecks.
  - Metrics: `cpu_usage_percentage`, `cpu_idle`, `cpu_load_1min`, `cpu_load_5min`, `cpu_load_15min`.
- **Memory Utilization**
  - Monitor RAM usage and track the swap usage.
  - Metrics: `total_memory`, `used_memory`, `free_memory`, `swap_usage`.
- **Disk I/O**
  - Track disk reads and writes, disk utilization, and latency.
  - Metrics: `disk_read_ops`, `disk_write_ops`, `disk_io_time`, `disk_read_bytes`, `disk_write_bytes`, `disk_utilization`.
- **Network Usage**
  - Track inbound and outbound traffic, packet loss, latency, and error rates.
  - Metrics: `network_in`, `network_out`, `network_error`, `packet_loss`, `latency`.

### **2. Application Metrics**
- **Application Response Time**
  - Measure how long it takes for requests to be processed by the application.
  - Metrics: `request_duration`, `response_time`.
- **Throughput**
  - Track the number of requests processed per second or minute.
  - Metrics: `requests_per_second`, `queries_per_second`.
- **Error Rates**
  - Monitor application-level errors such as HTTP 500 or application exceptions.
  - Metrics: `error_rate`, `request_errors`, `500_errors`.
- **Service Availability/Health**
  - Track if the service or application is running as expected.
  - Metrics: `service_up_time`, `service_health`.
- **Concurrency/Throughput**
  - Track the number of concurrent users or active sessions at any given time.
  - Metrics: `active_connections`, `concurrent_sessions`.

### **3. Database Metrics**
- **Query Performance**
  - Track slow or long-running queries.
  - Metrics: `query_duration`, `slow_queries`, `query_latency`.
- **Database Connections**
  - Monitor the number of active database connections.
  - Metrics: `active_connections`, `max_connections`.
- **Read/Write Throughput**
  - Track how much data is read from and written to the database.
  - Metrics: `read_ops`, `write_ops`, `data_read`, `data_written`.
- **Replication Lag**
  - Monitor the delay between primary and replica databases.
  - Metrics: `replica_lag`, `replication_health`.
- **Database Errors**
  - Track errors related to database queries.
  - Metrics: `database_errors`, `query_failures`.

### **4. Server Logs Monitoring**
- **Application Logs**
  - Analyze logs for errors, exceptions, and warnings from the application.
  - Look for high-frequency logs, fatal errors, and critical events.
  - Tools: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk, Fluentd.
- **System Logs**
  - Track events related to the server’s operating system (e.g., crashes, hardware failures).
  - Metrics: `kernel_logs`, `system_crashes`, `hardware_errors`.
- **Security Logs**
  - Monitor for security breaches, failed login attempts, and unauthorized access.
  - Metrics: `failed_logins`, `unauthorized_access`, `malicious_activity`.
- **Access Logs**
  - Track access logs for web servers (e.g., Apache, Nginx) to monitor traffic patterns, errors, and requests.
  - Metrics: `successful_requests`, `404_errors`, `5xx_errors`.
- **Audit Logs**
  - Monitor logs related to system changes, user activities, or administrative actions.
  - Metrics: `user_activity`, `admin_actions`, `permission_changes`.

### **5. Hardware Monitoring Metrics**
- **Temperature & Power Metrics**
  - Track server hardware temperature (CPU, GPU, motherboard) and power consumption.
  - Metrics: `cpu_temperature`, `gpu_temperature`, `server_power_usage`.
- **Hardware Failures**
  - Monitor for hardware failures like hard drive issues, memory faults, and system crashes.
  - Metrics: `disk_health`, `memory_faults`, `hardware_failure`.

### **6. Cloud Infrastructure Metrics (for cloud-based servers)**
- **Instance Health**
  - Monitor cloud instance performance, CPU, memory, and network usage.
  - Metrics: `cpu_usage`, `ram_usage`, `network_in`, `network_out`.
- **Auto-scaling Events**
  - Track scaling activities, like the launching or termination of instances.
  - Metrics: `auto_scaling_event`, `scaling_activity`.
- **Storage Metrics**
  - Monitor cloud storage utilization, throughput, and latency.
  - Metrics: `storage_used`, `storage_read_latency`, `storage_write_latency`.

### **7. Security Metrics**
- **Authentication and Authorization**
  - Track login attempts, access control errors, and privilege escalation.
  - Metrics: `failed_logins`, `unauthorized_access`, `permission_changes`.
- **Intrusion Detection**
  - Monitor for intrusion attempts and anomaly detection.
  - Metrics: `intrusion_attempts`, `anomalies_detected`.

### **8. Container Metrics (if using containers like Docker)**
- **Container Resource Usage**
  - Track CPU, memory, and disk usage of containers.
  - Metrics: `container_cpu_usage`, `container_memory_usage`, `container_disk_usage`.
- **Container Health**
  - Monitor container uptime, failures, and restarts.
  - Metrics: `container_uptime`, `container_restarts`, `container_health`.
- **Orchestrator Metrics (e.g., Kubernetes)**
  - Monitor pod status, node performance, and cluster health.
  - Metrics: `pod_status`, `node_cpu_usage`, `k8s_cluster_health`.

### **9. Network Metrics**
- **Latency and Throughput**
  - Measure latency between servers or external services and throughput on network interfaces.
  - Metrics: `network_latency`, `network_throughput`.
- **Packet Loss & Errors**
  - Monitor for dropped packets or network-related errors.
  - Metrics: `packet_loss`, `network_errors`.
- **Firewall/Firewall Logs**
  - Track traffic blocked or allowed by firewalls.
  - Metrics: `firewall_traffic`, `firewall_logs`.

### **10. User Experience Metrics (if user-facing applications)**
- **Page Load Time**
  - Measure how quickly your website or application loads for end users.
  - Metrics: `page_load_time`, `server_response_time`.
- **Transaction Latency**
  - Track the time it takes for a transaction to complete from start to finish.
  - Metrics: `transaction_latency`, `transaction_success_rate`.
  
### **11. Alerts and Thresholds**
- **Thresholds for Alerts**
  - Set thresholds for critical metrics such as CPU, memory, and disk usage.
  - Trigger alerts when these thresholds are exceeded.

"""
   
log_action("admin_user1", "Logged in")
log_action("admin_user1", "Deleted user", "User ID: 12345")
