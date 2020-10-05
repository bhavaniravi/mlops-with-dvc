---
apiVersion: "v1"
kind: "Namespace"
metadata:
  name: "mlops"
---
apiVersion: "apps/v1"
kind: "Deployment"
metadata:
  name: "mlops"
  namespace: "mlops"
  labels:
    app: "mlops"
spec:
  replicas: 1
  selector:
    matchLabels:
      app: "mlops"
  template:
    metadata:
      labels:
        app: "mlops"
    spec:
      containers:
      - name: "mlops-image-1"
        image: "gcr.io/GOOGLE_CLOUD_PROJECT/APP_NAME:COMMIT_SHA"
---
apiVersion: "autoscaling/v2beta1"
kind: "HorizontalPodAutoscaler"
metadata:
  name: "mlops-hpa-dbv6"
  namespace: "mlops"
  labels:
    app: "mlops"
spec:
  scaleTargetRef:
    kind: "Deployment"
    name: "mlops"
    apiVersion: "apps/v1"
  minReplicas: 1
  maxReplicas: 5
  metrics:
  - type: "Resource"
    resource:
      name: "cpu"
      targetAverageUtilization: 80
