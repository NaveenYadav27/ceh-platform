#!/bin/bash
echo "[+] Starting CEHv13 LMS Production Deployment..."

echo "[+] Building docker containers..."
docker-compose build

echo "[+] Starting services..."
docker-compose up -d

echo "[+] Deployment successful. LMS is running at http://localhost:3001"
