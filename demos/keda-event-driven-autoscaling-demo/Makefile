IMAGE ?= keda-redis-worker:0.1.0
KIND_CLUSTER ?= keda-demo
NAMESPACE ?= keda-demo

.PHONY: image kind-load deploy delete watch logs produce

image:
	docker build -t $(IMAGE) ./app

kind-load:
	kind load docker-image $(IMAGE) --name $(KIND_CLUSTER)

deploy:
	kubectl apply -k ./k8s

delete:
	kubectl delete -k ./k8s

watch:
	kubectl -n $(NAMESPACE) get pods,hpa,scaledobject -w

logs:
	kubectl -n $(NAMESPACE) logs deploy/keda-worker -f

produce:
	kubectl -n $(NAMESPACE) delete job keda-producer --ignore-not-found
	kubectl apply -f ./k8s/producer-job.yaml
