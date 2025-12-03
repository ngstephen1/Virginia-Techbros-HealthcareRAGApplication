<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# VIRGINIA-TECHBROS-IBM HEALTHCARE RAG APPLICATION

<em>IBM - Transforming Healthcare Insights with AI Power</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/ngstephen1/Virginia-Techbros-HealthcareRAGApplication?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/ngstephen1/Virginia-Techbros-HealthcareRAGApplication?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/ngstephen1/Virginia-Techbros-HealthcareRAGApplication?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/ngstephen1/Virginia-Techbros-HealthcareRAGApplication?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Keras-D00000.svg?style=flat&logo=Keras&logoColor=white" alt="Keras">
<img src="https://img.shields.io/badge/npm-CB3837.svg?style=flat&logo=npm&logoColor=white" alt="npm">
<img src="https://img.shields.io/badge/Redis-FF4438.svg?style=flat&logo=Redis&logoColor=white" alt="Redis">
<img src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=flat&logo=TensorFlow&logoColor=white" alt="TensorFlow">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
<br>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/Rich-FAE742.svg?style=flat&logo=Rich&logoColor=black" alt="Rich">
<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat&logo=Gunicorn&logoColor=white" alt="Gunicorn">
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat&logo=React&logoColor=black" alt="React">
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Virginia-Techbros-HealthcareRAGApplication is a robust, full-stack platform tailored for healthcare research and medical literature synthesis. It combines a scalable microservices architecture with advanced retrieval and AI capabilities to deliver accurate, citation-backed insights. The core features include:

- 🧩 **Modular Architecture:** Orchestrates React, Flask, MongoDB, and vector stores within Docker Compose for flexible deployment.
- 🚀 **Retrieval-Augmented Generation:** Enables efficient multi-document ingestion, search, and synthesis of medical literature.
- 🔍 **Scalable Vector Search:** Integrates Milvus and IBM Watsonx for high-performance embedding storage and retrieval.
- 📄 **Document Processing:** Automates PDF chunking, index building, and offline querying workflows.
- ⚙️ **Developer-Friendly:** Containerized setup with automation scripts for environment setup, testing, and evaluation.
- 🌐 **Healthcare Focus:** Designed to support evidence-based medical research with citation accuracy.

---

## Features

|      | Component            | Details                                                                                                              |
| :--- | :------------------- | :------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**     | <ul><li>Microservices architecture with separate frontend and backend components</li><li>Backend built with Flask</li><li>Frontend developed with React</li></ul> |
| 🔩 | **Code Quality**     | <ul><li>Standard project structure with clear separation of concerns</li><li>Use of package.json and requirements.txt for dependency management</li><li>Consistent naming conventions</li></ul> |
| 📄 | **Documentation**    | <ul><li>Docker-related docs: docker-compose.yml, Dockerfiles for frontend and backend</li><li>README.md provides project overview and setup instructions</li></ul> |
| 🔌 | **Integrations**     | <ul><li>Containerization via Docker and Docker Compose</li><li>Package managers: npm for frontend, pip for backend</li><li>Potential cloud integrations with boto3 and s3transfer</li></ul> |
| 🧩 | **Modularity**       | <ul><li>Frontend and backend codebases modularized in separate directories</li><li>Use of Flask blueprints or similar for backend modularity (implied)</li></ul> |
| 🧪 | **Testing**          | <ul><li>Testing libraries included: @testing-library/react, @testing-library/jest-dom, @testing-library/user-event</li><li>Likely React component tests and backend tests with pytest (implied by requirements.txt)</li></ul> |
| ⚡️  | **Performance**      | <ul><li>Use of optimized libraries like TensorFlow, OpenCV, and PyTorch for ML tasks</li><li>Containerized deployment for scalable performance</li></ul> |
| 🛡️ | **Security**         | <ul><li>Cross-Origin Resource Sharing (CORS) handled via Flask-Cors</li><li>Secure dependencies with version pinning in requirements.txt</li></ul> |
| 📦 | **Dependencies**     | <ul><li>Frontend: React, react-dom, react-scripts, markdown</li><li>Backend: Flask, Flask-Cors, TensorFlow, OpenCV, boto3, and numerous ML and utility libraries</li></ul> |

---

## Project Structure

```sh
└── Virginia-Techbros-HealthcareRAGApplication/
    ├── 0
    ├── Dockerfile.backend
    ├── Dockerfile.frontend
    ├── Makefile
    ├── README.md
    ├── README.txt
    ├── backend
    │   ├── Dockerfile
    │   ├── __init__.py
    │   ├── data
    │   └── server
    ├── chunks
    │   ├── 46a2bb5d.jsonl
    │   ├── Advancement_AI.jsonl
    │   ├── Efficacy_Diabetes.jsonl
    │   ├── Stability_mRNA_Vaccines.jsonl
    │   ├── Stem_Cell_Therapy.jsonl
    │   ├── b6eaed7b.jsonl
    │   ├── c2c6f0c8.jsonl
    │   ├── demo.jsonl
    │   └── mRNA_Vaccine_Tech.jsonl
    ├── docker-compose.yml
    ├── eval
    │   └── gold.jsonl
    ├── frontend
    │   └── healthcare-rag
    ├── scripts
    │   ├── build_index.py
    │   ├── build_vector_store.py
    │   ├── offline_query.py
    │   └── run_chunker.py
    └── server
        ├── __init__.py
        ├── __pycache__
        ├── contracts
        ├── embeddings
        ├── generate
        └── retrieval
```

---

### Project Index

<details open>
	<summary><b><code>VIRGINIA-TECHBROS-HEALTHCARERAGAPPLICATION/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Defines project automation tasks for setting up the environment, installing dependencies, building the search index, executing offline queries, evaluating performance, and cleaning generated data<br>- Facilitates streamlined workflows across development, testing, and evaluation phases, ensuring consistent setup and execution within the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/docker-compose.yml'>docker-compose.yml</a></b></td>
					<td style='padding: 8px;'>- Defines a multi-service Docker Compose setup orchestrating a research-focused application<br>- It integrates a React/Nginx frontend, a Flask backend with a RAG pipeline, and a MongoDB database, enabling seamless development and deployment<br>- Facilitates inter-service communication, persistent data storage, and environment configuration, supporting a scalable architecture for research and experimentation workflows.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/README.md'>README.md</a></b></td>
					<td style='padding: 8px;'>- Facilitates the integration and orchestration of the AI Medical Research Synthesis Agent within the project architecture, enabling efficient retrieval and synthesis of medical literature<br>- Supports the core functionality of ingesting multiple documents, leveraging retrieval-augmented generation to produce accurate, citation-backed insights for medical researchers<br>- Ensures seamless coordination among components to deliver trustworthy, evidence-based answers.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/Dockerfile.backend'>Dockerfile.backend</a></b></td>
					<td style='padding: 8px;'>- Sets up the backend application environment by defining the Python runtime, installing dependencies, and configuring the server to run the backend server module<br>- It ensures the backend service is properly containerized, accessible on port 8000, and ready to handle API requests within the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/0'>0</a></b></td>
					<td style='padding: 8px;'>Certainly! Please provide the project structure, file path, and file content so I can generate the appropriate summary for you.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/README.txt'>README.txt</a></b></td>
					<td style='padding: 8px;'>- Provides an overview of the AI-powered medical research synthesis agent, facilitating multi-document ingestion, analysis, and citation within a healthcare-focused web application<br>- It supports efficient summarization and retrieval of relevant scientific literature, ensuring trustworthy, well-cited outputs<br>- The component integrates document processing, retrieval, and AI synthesis to streamline researchers access to accurate, organized medical insights.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/Dockerfile.frontend'>Dockerfile.frontend</a></b></td>
					<td style='padding: 8px;'>- Defines the deployment process for the frontend application by building optimized static assets with Node.js and serving them via Nginx<br>- It ensures a streamlined transition from development to production, enabling efficient delivery of the user interface within the overall architecture<br>- This setup supports scalable, performant frontend delivery aligned with the projects microservices-oriented structure.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- scripts Submodule -->
	<details>
		<summary><b>scripts</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ scripts</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/scripts/build_vector_store.py'>build_vector_store.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates the creation of a vector store by fetching data from an external API, enabling efficient storage and retrieval of embeddings within the overall architecture<br>- Supports the project’s goal of building a scalable, searchable knowledge base or retrieval system, integrating external data sources seamlessly into the vector-based infrastructure.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/scripts/run_chunker.py'>run_chunker.py</a></b></td>
					<td style='padding: 8px;'>- Generates overlapping text chunks from medical research PDFs to facilitate efficient indexing and retrieval<br>- Integrates document processing into the broader architecture by preparing data for downstream tasks such as search, analysis, or machine learning, ensuring consistent formatting and segmentation across the dataset.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/scripts/offline_query.py'>offline_query.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates retrieval and synthesis of relevant information from a knowledge base by embedding user queries, ranking document snippets based on similarity, and generating concise summaries with citations<br>- Supports offline question-answering workflows within the broader system architecture, enabling efficient extraction of key insights from stored data for user inquiries.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/scripts/build_index.py'>build_index.py</a></b></td>
					<td style='padding: 8px;'>- Builds and updates vector representations of text chunks by embedding data and storing it in both a local memory index and a Milvus vector database<br>- Facilitates efficient retrieval and similarity search within the larger architecture, supporting scalable, high-performance semantic search capabilities across the dataset.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- backend Submodule -->
	<details>
		<summary><b>backend</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ backend</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Sets up the backend environment by configuring the Python runtime, installing dependencies, and defining the command to launch the server<br>- Facilitates containerized deployment of the backend application, ensuring consistent execution and accessibility on port 8000 within the overall architecture.</td>
				</tr>
			</table>
			<!-- server Submodule -->
			<details>
				<summary><b>server</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ backend.server</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/server.py'>server.py</a></b></td>
							<td style='padding: 8px;'>- Provides RESTful API endpoints for document ingestion, health checks, and conversational querying within a PDF-centric knowledge management system<br>- Facilitates PDF validation, document storage, retrieval, and question-answering by integrating vector search, language models, and external services, thereby enabling seamless interaction with stored documents and supporting dynamic information retrieval and summarization workflows.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/requirements.txt'>requirements.txt</a></b></td>
							<td style='padding: 8px;'>- Defines the essential dependencies for the backend server, supporting core functionalities such as AI model inference, data processing, web API endpoints, and cloud integrations<br>- Ensures a consistent environment for deploying scalable, feature-rich services within the overall architecture, facilitating seamless interaction between machine learning components, data workflows, and client interfaces.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/orchestrator.py'>orchestrator.py</a></b></td>
							<td style='padding: 8px;'>- Facilitates medical research question answering by constructing prompts from relevant snippets, invoking an external language model, and ensuring responses are grounded in provided evidence<br>- Integrates validation and fallback mechanisms to maintain answer integrity, supporting the broader architectures goal of delivering accurate, citation-backed insights within a research-oriented system.</td>
						</tr>
					</table>
					<!-- api Submodule -->
					<details>
						<summary><b>api</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ backend.server.api</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/api/app.py'>app.py</a></b></td>
									<td style='padding: 8px;'>- Provides core API endpoints for document ingestion, querying, and retrieval within the backend architecture<br>- Facilitates saving PDFs, executing hybrid search with embeddings and vector stores, and synthesizing answers with citations<br>- Serves as the primary interface connecting data ingestion, retrieval, and response generation, enabling seamless interaction with the document processing and question-answering system.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- vector Submodule -->
					<details>
						<summary><b>vector</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ backend.server.vector</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/vector/milvus_store.py'>milvus_store.py</a></b></td>
									<td style='padding: 8px;'>- Facilitates efficient storage and retrieval of medical document embeddings by interfacing with Milvus, a vector similarity search engine<br>- Handles collection creation, data upsertion, and similarity searches, with fallback to in-memory search when Milvus is unavailable<br>- Supports scalable, high-performance retrieval of relevant medical information based on vector similarity, integral to the overall medical retrieval and question-answering architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/vector/wx_adapter.py'>wx_adapter.py</a></b></td>
									<td style='padding: 8px;'>- Provides an interface to generate text embeddings via IBM watsonx.ai API, enabling semantic understanding within the application<br>- It manages API authentication, handles token refreshes, and offers fallback mock vectors for robustness<br>- Integral to the architecture, it supports efficient vectorization of textual data, facilitating downstream tasks like search, classification, or recommendation systems.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- retrieval Submodule -->
					<details>
						<summary><b>retrieval</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ backend.server.retrieval</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/retrieval/hybrid.py'>hybrid.py</a></b></td>
									<td style='padding: 8px;'>- Implements a hybrid retrieval strategy combining vector similarity search with BM25 reranking to identify the most relevant documents for a given query<br>- It enhances search accuracy by first narrowing candidates through embedding-based search, then refining results with BM25 scoring, supporting effective information retrieval within the overall architecture.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- generate Submodule -->
					<details>
						<summary><b>generate</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ backend.server.generate</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/generate/answer.py'>answer.py</a></b></td>
									<td style='padding: 8px;'>- Generates structured, developer-focused answers by extracting key snippets from relevant documents, including citations and source details<br>- Facilitates clear, concise responses for question-answering workflows, supporting integration with external AI services for enhanced synthesis<br>- Serves as a core component in delivering accurate, traceable information within the overall backend architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/generate/validators.py'>validators.py</a></b></td>
									<td style='padding: 8px;'>- Provides validation utilities for managing citation references within user responses<br>- Facilitates extraction of used IDs, removal of orphaned references beyond a specified maximum, and detection of any citations<br>- These functions support maintaining consistent and accurate citation formatting across the backend, ensuring data integrity and coherence within the overall system architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/generate/granite_adapter.py'>granite_adapter.py</a></b></td>
									<td style='padding: 8px;'>- Facilitates interaction with IBM Watsonx.ai Granite for text generation within the backend architecture<br>- Handles authentication, constructs requests, and retrieves generated content based on prompts, supporting the overall AI-powered content creation capabilities of the system<br>- Ensures seamless integration with IBMs cloud services to enable scalable, cloud-based natural language processing.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- ingest Submodule -->
					<details>
						<summary><b>ingest</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ backend.server.ingest</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/ingest/save_only.py'>save_only.py</a></b></td>
									<td style='padding: 8px;'>- Facilitates the storage of uploaded PDF documents by saving them to a designated directory with unique identifiers<br>- Integrates seamlessly into the backend ingestion pipeline, ensuring reliable persistence of files for subsequent processing or retrieval within the overall system architecture<br>- This component supports scalable document management by maintaining organized and accessible document storage.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- core Submodule -->
					<details>
						<summary><b>core</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ backend.server.core</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/backend/server/core/config.py'>config.py</a></b></td>
									<td style='padding: 8px;'>- Defines centralized configuration and initializes shared instances of WatsonEmbedder and MilvusStore for the application<br>- Facilitates seamless access to embedding and vector store services across the codebase, supporting efficient management of medical papers and document indexing within the backend architecture<br>- Ensures consistent setup and environment variable handling for core components.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- frontend Submodule -->
	<details>
		<summary><b>frontend</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ frontend</b></code>
			<!-- healthcare-rag Submodule -->
			<details>
				<summary><b>healthcare-rag</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ frontend.healthcare-rag</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/README.md'>README.md</a></b></td>
							<td style='padding: 8px;'>- Provides the foundational structure for the healthcare-related web application, enabling user interaction and interface rendering<br>- It orchestrates the client-side experience, integrating React components to facilitate seamless navigation, data display, and user engagement within the broader system architecture<br>- This setup ensures a responsive, maintainable frontend aligned with backend services for healthcare data management.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/package.json'>package.json</a></b></td>
							<td style='padding: 8px;'>- Defines the frontend configuration and dependencies for the healthcare-rag project, enabling a React-based user interface<br>- It orchestrates development, testing, and build processes, serving as the foundation for the client-side application that interacts with backend services<br>- This setup ensures a consistent environment for delivering healthcare-related features within the overall system architecture.</td>
						</tr>
					</table>
					<!-- src Submodule -->
					<details>
						<summary><b>src</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ frontend.healthcare-rag.src</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/index.js'>index.js</a></b></td>
									<td style='padding: 8px;'>- Initialize and render the main React application within the healthcare-rag project, establishing the entry point for the frontend interface<br>- It connects the core App component to the DOM, enabling the user interface to load and function correctly within the overall architecture<br>- This setup ensures the seamless startup of the web application for healthcare-related interactions.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/App.jsx'>App.jsx</a></b></td>
									<td style='padding: 8px;'>- Orchestrates the core user interactions within the healthcare RAG application by managing state, data fetching, and communication with backend APIs<br>- Facilitates conversation flow, document management, and query processing, ensuring seamless integration of chat, document upload, and history features<br>- Serves as the central hub for coordinating frontend components and maintaining synchronized data across the application architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/index.html'>index.html</a></b></td>
									<td style='padding: 8px;'>- Sets up the foundational HTML structure for the ResearchBot AI Literature Synthesis application, establishing the main container for React rendering, loading essential styles and fonts, and integrating the primary JavaScript bundle<br>- It enables the web interface to function seamlessly within the broader architecture, facilitating user interaction with the AI-powered research synthesis features.</td>
								</tr>
							</table>
							<!-- utils Submodule -->
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ frontend.healthcare-rag.src.utils</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/utils/constants.jsx'>constants.jsx</a></b></td>
											<td style='padding: 8px;'>- Defines key constants for the healthcare RAG frontend, including visual styling, maximum document limits, and the backend API base URL<br>- These constants ensure consistent UI appearance and facilitate seamless communication with the Flask backend, supporting the overall architecture by standardizing configuration values across the application.</td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/utils/api.js'>api.js</a></b></td>
											<td style='padding: 8px;'>- Provides a unified interface for frontend interactions with the Flask backend API, managing document handling, conversation lifecycle, messaging, and AI-powered RAG queries<br>- Facilitates seamless data exchange and state management within the healthcare RAG application, supporting core functionalities such as document ingestion, conversation flow, and user-AI interactions essential to the platforms architecture.</td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- hooks Submodule -->
							<details>
								<summary><b>hooks</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ frontend.healthcare-rag.src.hooks</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/hooks/useDataFetcher.js'>useDataFetcher.js</a></b></td>
											<td style='padding: 8px;'>- Provides a custom React hook that manages data fetching for healthcare-related conversations, documents, and messages<br>- It centralizes state management and handles asynchronous API calls to retrieve and update relevant data, ensuring the frontend stays synchronized with backend data sources<br>- This hook facilitates seamless data updates and loading state management within the applications healthcare communication interface.</td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- mui-refactor Submodule -->
							<details>
								<summary><b>mui-refactor</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ frontend.healthcare-rag.src.mui-refactor</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/mui-refactor/refactor.jsx'>refactor.jsx</a></b></td>
											<td style='padding: 8px;'>- Refactor.jsxThis component serves as the core user interface for the healthcare retrieval-augmented generation (RAG) application<br>- It orchestrates the layout and interaction flow, enabling users to upload, view, and manage documents, initiate chat sessions, and review conversation history<br>- By integrating Material-UI components and custom theming, it provides a cohesive and accessible frontend experience that facilitates seamless user engagement with the underlying healthcare data retrieval and AI-powered response generation functionalities within the broader application architecture.</td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- config Submodule -->
							<details>
								<summary><b>config</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ frontend.healthcare-rag.src.config</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/config/theme.js'>theme.js</a></b></td>
											<td style='padding: 8px;'>- Defines the visual theme and styling conventions for the healthcare RAG applications frontend, ensuring a consistent user interface aligned with IBM branding<br>- Establishes color schemes, typography, and component styles to enhance usability and aesthetic coherence across the platform<br>- This configuration supports a unified look and feel within the overall application architecture.</td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- components Submodule -->
							<details>
								<summary><b>components</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ frontend.healthcare-rag.src.components</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Header.jsx'>Header.jsx</a></b></td>
											<td style='padding: 8px;'>- Provides a consistent header component that displays branding, document upload status, and a button to initiate new conversations, supporting user navigation and interaction within the healthcare research application<br>- It enhances the overall user experience by offering clear visual cues and quick access to core functionalities, integrating seamlessly into the applications architecture.</td>
										</tr>
									</table>
									<!-- Input Submodule -->
									<details>
										<summary><b>Input</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ frontend.healthcare-rag.src.components.Input</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Input/TabNavigation.jsx'>TabNavigation.jsx</a></b></td>
													<td style='padding: 8px;'>- Provides a bottom navigation bar for switching between chat, document uploads, and conversation history within the healthcare RAG frontend<br>- It dynamically displays counts for uploaded documents and past conversations, enhancing user interaction and navigation flow across core sections of the application.</td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Input/QueryInput.jsx'>QueryInput.jsx</a></b></td>
													<td style='padding: 8px;'>- Facilitates user interaction by providing an input interface for submitting research or general queries to the AI<br>- It dynamically adjusts prompts based on uploaded documents and manages user input, submission, and processing states<br>- Integrates seamlessly into the overall architecture to enable intuitive, real-time question-answering capabilities within the healthcare research application.</td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- Documents Submodule -->
									<details>
										<summary><b>Documents</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ frontend.healthcare-rag.src.components.Documents</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Documents/DocumentItem.jsx'>DocumentItem.jsx</a></b></td>
													<td style='padding: 8px;'>- Render individual uploaded documents within the healthcare application, providing visual identification, upload date, and a delete option<br>- Facilitates user management of documents by enabling easy review and removal, integrating seamlessly into the broader document handling and user interface architecture of the frontend<br>- Enhances user experience through clear presentation and interactive controls.</td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Documents/DocumentManager.jsx'>DocumentManager.jsx</a></b></td>
													<td style='padding: 8px;'>- Facilitates document upload and management within the healthcare RAG application, enabling users to add, view, and delete research papers or articles in PDF or text format<br>- Supports citation-backed analysis by maintaining an organized list of uploaded documents, ensuring adherence to maximum upload limits, and integrating seamlessly into the overall data processing workflow.</td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- Chat Submodule -->
									<details>
										<summary><b>Chat</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ frontend.healthcare-rag.src.components.Chat</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Chat/QueryInput.jsx'>QueryInput.jsx</a></b></td>
													<td style='padding: 8px;'>- Facilitates user interaction by providing a responsive input interface for submitting research or general queries within the healthcare research assistant application<br>- It dynamically adjusts prompts based on uploaded documents, manages input state, and indicates processing status, enabling seamless communication with backend AI services to generate relevant responses<br>- This component is central to user engagement and query handling in the overall architecture.</td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Chat/MessageBubble.jsx'>MessageBubble.jsx</a></b></td>
													<td style='padding: 8px;'>- Render individual chat messages with styling that distinguishes between user and system roles, enhancing readability and user experience within the healthcare RAG applications chat interface<br>- The component dynamically formats message content, timestamps, and role labels, contributing to a clear and intuitive conversation flow in the overall frontend architecture.</td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/Chat/ChatInterface.jsx'>ChatInterface.jsx</a></b></td>
													<td style='padding: 8px;'>- Render the main chat interface, displaying either a welcoming prompt or a sequence of message bubbles based on user interactions<br>- Facilitates user engagement by presenting conversation history and guiding users to upload documents or ask questions, thereby supporting the overall architecture of an interactive healthcare research assistant with citation-backed responses.</td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- common Submodule -->
									<details>
										<summary><b>common</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ frontend.healthcare-rag.src.components.common</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/common/TabNavigation.jsx'>TabNavigation.jsx</a></b></td>
													<td style='padding: 8px;'>- Provides a tabbed navigation component for the healthcare application, enabling users to switch seamlessly between chat, uploaded documents, and conversation history<br>- It dynamically displays counts for documents and conversations, enhancing user awareness of available data<br>- Integrates with the overall UI architecture to facilitate intuitive access to core features within the frontends modular component structure.</td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/common/Header.jsx'>Header.jsx</a></b></td>
													<td style='padding: 8px;'>- Provides a header component for the ResearchBot web interface, displaying the application title, a subtitle, current document upload status, and a button to initiate new conversations<br>- It enhances user navigation and interaction within the overall architecture, supporting seamless access to core functionalities of the AI Literature Analysis Assistant.</td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- History Submodule -->
									<details>
										<summary><b>History</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ frontend.healthcare-rag.src.components.History</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/History/HistorySidebar.jsx'>HistorySidebar.jsx</a></b></td>
													<td style='padding: 8px;'>- Displays a list of past healthcare-related conversations, enabling users to review, select, or delete previous interactions<br>- Integrates with conversation management functions to facilitate seamless navigation through conversation history, supporting an intuitive user experience within the healthcare applications chat interface.</td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/components/History/HistoryItem.jsx'>HistoryItem.jsx</a></b></td>
													<td style='padding: 8px;'>- Render individual conversation entries within the history panel, enabling users to load or delete specific conversations<br>- Facilitates seamless interaction by visually highlighting the active conversation and providing intuitive controls for managing conversation history, thereby supporting efficient navigation and management of past interactions within the healthcare RAG applications user interface.</td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- services Submodule -->
							<details>
								<summary><b>services</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ frontend.healthcare-rag.src.services</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/services/constants.jsx'>constants.jsx</a></b></td>
											<td style='padding: 8px;'>- Defines key constants for the healthcare retrieval-augmented generation application, including visual styling, maximum document limits, and the backend API endpoint<br>- These constants ensure consistent configuration and appearance across the frontend, facilitating seamless integration with the backend services and maintaining a cohesive user interface within the overall architecture.</td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/frontend/healthcare-rag/src/services/apiService.js'>apiService.js</a></b></td>
											<td style='padding: 8px;'>- Facilitates communication between the frontend and backend by providing mock API functions for managing documents, conversations, messages, and query processing within the healthcare research application<br>- Supports data retrieval, creation, deletion, and simulated query responses, enabling seamless integration and testing of the applications core data interactions and retrieval-augmented generation workflows.</td>
										</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- server Submodule -->
	<details>
		<summary><b>server</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ server</b></code>
			<!-- contracts Submodule -->
			<details>
				<summary><b>contracts</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ server.contracts</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/server/contracts/types.py'>types.py</a></b></td>
							<td style='padding: 8px;'>- Defines structured data types for representing document segments and search results within the server architecture<br>- These types facilitate consistent handling of document chunks and search hits, supporting efficient querying, indexing, and retrieval processes across the system<br>- They serve as foundational data contracts that ensure clarity and interoperability in managing document-related information throughout the application.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/server/contracts/vector_store.py'>vector_store.py</a></b></td>
							<td style='padding: 8px;'>- Defines a protocol for interacting with a vector store, enabling storage and retrieval of vectorized data chunks<br>- Facilitates seamless integration of different vector database implementations within the overall architecture, supporting efficient similarity searches and data management essential for scalable, AI-driven applications<br>- Ensures consistent interface adherence across various vector store implementations in the project.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/server/contracts/embedder.py'>embedder.py</a></b></td>
							<td style='padding: 8px;'>- Defines a contract for embedding models to convert textual data into numerical vector representations<br>- Serves as a key interface within the architecture, enabling interchangeable embedding implementations for downstream tasks such as similarity search or semantic analysis<br>- Ensures consistency and flexibility across different embedder modules, facilitating seamless integration and scalability within the overall system.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- retrieval Submodule -->
			<details>
				<summary><b>retrieval</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ server.retrieval</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/server/retrieval/discovery_adapter.py'>discovery_adapter.py</a></b></td>
							<td style='padding: 8px;'>- Facilitates integration with IBM Watsonx Discovery to perform document retrieval based on user queries, returning relevant hits for downstream processing<br>- Serves as a key component within the retrieval architecture, enabling the system to leverage external knowledge sources for enhanced information access and supporting the overall search and discovery functionality of the platform.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- embeddings Submodule -->
			<details>
				<summary><b>embeddings</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ server.embeddings</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/master/server/embeddings/wx_adapter.py'>wx_adapter.py</a></b></td>
							<td style='padding: 8px;'>- Provides a lightweight fallback embedding mechanism for the project, enabling text vectorization without external dependencies<br>- It facilitates integration with IBM watsonx.ai embeddings by offering a simple, pure-Python method to generate numerical representations of text, supporting the overall architectures goal of flexible and extensible embedding capabilities.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Npm, Pip
- **Container Runtime:** Docker

### Installation

Build Virginia-Techbros-HealthcareRAGApplication from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Virginia-Techbros-HealthcareRAGApplication
    ```

3. **Install the dependencies:**

**Using [docker](https://www.docker.com/):**

```sh
❯ docker build -t ngstephen1/Virginia-Techbros-HealthcareRAGApplication .
```
**Using [npm](https://www.npmjs.com/):**

```sh
❯ npm install
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r backend/server/requirements.txt
```

### Usage

Run the project with:

**Using [docker](https://www.docker.com/):**

```sh
docker run -it {image_name}
```
**Using [npm](https://www.npmjs.com/):**

```sh
npm start
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
python {entrypoint}
```

### Testing

Virginia-techbros-healthcareragapplication uses the {__test_framework__} test framework. Run the test suite with:

**Using [docker](https://www.docker.com/):**

```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [npm](https://www.npmjs.com/):**

```sh
npm test
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
pytest
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/issues)**: Submit bugs found or log feature requests for the `Virginia-Techbros-HealthcareRAGApplication` project.
- **💡 [Submit Pull Requests](https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ngstephen1/Virginia-Techbros-HealthcareRAGApplication
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/ngstephen1/Virginia-Techbros-HealthcareRAGApplication/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ngstephen1/Virginia-Techbros-HealthcareRAGApplication">
   </a>
</p>
</details>

---

## License

Virginia-techbros-healthcareragapplication is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
