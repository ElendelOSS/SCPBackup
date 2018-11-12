# Makefile for building publishing container
PROJECT = fortigate-backup
VERSION = $(shell whoami)
REGISTRY = local
GITHASH = $(shell git rev-parse HEAD | cut -c 1-7)
APP_IMAGE = $(PROJECT):$(GITHASH)
CONTAINER_TAG = latest

imageLocal:
	docker build -t $(APP_IMAGE) .
.PHONY: imageLocal

imageOnly:
	docker build -t $(APP_IMAGE) .
.PHONY: image

image: imageOnly
	docker push $(APP_IMAGE) 
.PHONY: image

publish-image: image
	docker tag $(APP_IMAGE) $(REGISTRY)/$(PROJECT):$(GITHASH)
	docker tag $(APP_IMAGE) $(REGISTRY)/$(PROJECT):$(CONTAINER_TAG)
	docker push $(REGISTRY)/$(PROJECT):$(GITHASH)
	docker push $(REGISTRY)/$(PROJECT):$(CONTAINER_TAG)
.PHONY: publish-image

testLocal:
	docker build -f Dockerfile.test -t pystacks-local-test .
	docker build -f Dockerfile.check -t pystacks-local-check .
.PHONY: testLocal

coverageLocal:
	nosetests --with-coverage -v --cover-package=PyStacks --cover-html --cover-html-dir=coverage
	open ./coverage/index.html
.PHONY:coverageLocal

