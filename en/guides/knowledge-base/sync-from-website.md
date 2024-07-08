# Importing Data from Web Pages

Dify Knowledge Base supports web scraping and parsing into Markdown for import into the knowledge base through integration with Firecrawl.

**Note:**
[Firecrawl](https://www.firecrawl.dev/) is an open-source web parsing tool that converts web pages into clean and LLM-friendly Markdown format text. It also provides an easy-to-use API service.

### How to Configure

First, you need to configure Firecrawl credentials on the DataSource page.

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Log in to the [Firecrawl official website](https://www.firecrawl.dev/), complete the registration, obtain the API Key, and then fill it in and save.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

On the knowledge base creation page, select **Sync from website** and **enter the URL of the web page to be scraped**.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption><p>Web page scraping configuration</p></figcaption></figure>

The configuration items in the settings include: whether to scrape subpages, the maximum number of pages to scrape, the depth of page scraping, excluding pages, only scraping specific pages, and extracting content. After completing the configuration, click **Run** to preview the parsed pages.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Executing the scrape</p></figcaption></figure>

After importing the parsed text from the web page into the knowledge base documents, view the import results. Click **Add URL** to continue importing new web pages.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>Importing parsed web page text into the knowledge base</p></figcaption></figure>