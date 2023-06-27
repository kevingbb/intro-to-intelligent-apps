# Orchestrators

In this document you will find exercises for building large language models (LLMs) into applications. For each orchestrator you will see how to setup a sample project and turn a prompt into a callable API endpoint. Your task will be to call the API endpoint using curl or Postman to achieve the expected result.

The list below outlines some of the options for interacting and wrapping the Azure Open AI service. The first item in the list outlines how to interact with the raw Azure OpenAI API endpoint. This is not likely the best option for most scenarios, but it highlights what the underlying rest-based API looks like. The second item in the list is how to use the OpenAI packages and configure them for Azure OpenAI. The third item in the list is how to use the Semantic Kernel framework to wrap the Azure OpenAI API. The fourth item in the list is how to use Langchain to wrap the Azure OpenAI API.

The first two in the list are focused on the API structure and how to interact with the Azure OpenAI endpoints. The last two in the list are focused on how to orchestrate and chain multiple steps together which will then determine the appropriate way to interact with the Azure OpenAI API in a way that makes it easier to use in an application.

* [Azure OpenAI API](azureopenaiapi.md)
* [OpenAI Packages/Libraries](openai.md)
* [Semantic Kernel](semantickernel.md)
* [Langchain](langchain.md)
