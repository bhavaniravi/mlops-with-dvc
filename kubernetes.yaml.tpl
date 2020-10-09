---
apiVersion: "v1"
kind: "Namespace"
metadata:
  name: APP_NAME
---
apiVersion: "apps/v1"
kind: "Deployment"
metadata:
  name: APP_NAME
  namespace: APP_NAME
  labels:
    app: APP_NAME
spec:
  replicas: 1
  selector:
    matchLabels:
      app: APP_NAME
  template:
    metadata:
      labels:
        app: APP_NAME
    spec:
      containers:
      - name: "mlops-image-1"
        image: "gcr.io/GOOGLE_CLOUD_PROJECT/APP_NAME:COMMIT_SHA"
---
kind: Service
apiVersion: v1
metadata:
  namespace: "mlops"
  name: APP_NAME
spec:
  selector:
    app: APP_NAME
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    name: APP_NAME
  type: LoadBalancer

