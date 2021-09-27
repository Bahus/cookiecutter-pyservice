.DEFAULT_GOAL := help
.PHONY: $(MAKECMDGOALS)

check: ## check linters, pip requirements
	acme-tasks check-docker-compose

tests: ## tests application through docker-compose
	acme-tasks tests-docker-compose

deploy: ## deploy docker image
	acme-tasks cluster.deploy \
	--image-path $(APP_IMAGE_PATH) \
	--image-tag $(IMAGE_TAG) \
	--env $(ENVIRONMENT)
