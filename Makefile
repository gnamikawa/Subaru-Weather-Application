SHELL:=/bin/bash

export LocalRootDir=$(CURDIR)
export WebsiteDir=$(LocalRootDir)/website
export FigurebotDir=$(LocalRootDir)/figurebot

deploy: getdep wait build
getdep:
	@echo "[Begin] Installing SWA Dependencies..."
	@cd $(WebsiteDir);\
	npm install
	@echo "[Finished] Installing SWA Dependencies."

build:
	@echo "[Begin] Building SWA..."
	@cd $(WebsiteDir);\
	npm run build
	@echo "[Finished] Building SWA."
wait:
	@sleep 10
dataclean:
	@echo "[Begin] Cleaning Python Data..."
	@rm -vrf $(FigurebotDir)/Data/..?*
	@rm -vrf $(FigurebotDir)/Data/.[!.]*
	@rm -vrf $(FigurebotDir)/Data/*
	@echo "[Finished] Cleaning Python Data."
	
	@echo "[Begin] Cleaning Python Output..."
	@rm -vrf $(FigurebotDir)/Output/..?*
	@rm -vrf $(FigurebotDir)/Output/.[!.]*
	@rm -vrf $(FigurebotDir)/Output/*
	@echo "[Finished] Cleaning Python Output."

websiteclean:
	@echo "[Begin] Cleaning Dependencies..."
	@rm -vrf $(WebsiteDir)/node_modules/..?*
	@rm -vrf $(WebsiteDir)/node_modules/.[!.]*
	@rm -vrf $(WebsiteDir)/node_modules/*
	# @rmdir -v $(WebsiteDir)/node_modules/
	@echo "[Finished] Cleaning Dependencies."
	
	@echo "[Begin] Cleaning Build..."
	@rm -vrf $(WebsiteDir)/build/..?*
	@rm -vrf $(WebsiteDir)/build/.[!.]*
	@rm -vrf $(WebsiteDir)/build/*
	@echo "[Finished] Cleaning Build."

cleanall: websiteclean dataclean