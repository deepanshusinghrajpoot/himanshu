"""





# Firecrawl MCP – Website Page Discovery

## 1. Purpose
Use Firecrawl MCP to discover all publicly accessible pages and URLs of a website.

## 2. Important Firecrawl Tools

- `firecrawl_map`
  - Discovers website URLs.
  - Finds internal links.
  - Helps build a website sitemap.

- `firecrawl_crawl`
  - Visits multiple discovered pages.
  - Extracts page content.
  - Returns structured page information.

- `firecrawl_scrape`
  - Extracts content from an individual URL.

## 3. Website Discovery Workflow

Step 1: Provide the target website URL.
Step 2: Use `firecrawl_map` to discover URLs.
Step 3: Collect URLs from available sitemap and internal links.
Step 4: Remove duplicate URLs.
Step 5: Categorize discovered pages.
Step 6: Save the URL inventory in `website-sitemap.md`.
Step 7: Use `firecrawl_crawl` to extract content from important pages.


## 4. Page Categories

- Home
- About
- Services
- Products
- Blog / News
- Contact
- Login
- Registration
- Dashboard (only if publicly accessible)
- Other Pages


## 5. Information to Extract

- Total discovered pages
- Page URLs
- Page titles
- Page categories
- Internal links
- Nested URL structures
- Duplicate URLs
- Sitemap availability
- Discovery limitations


## 6. Important Limitations

- Firecrawl cannot guarantee discovery of every website page.
- Unlinked pages may not be discovered.
- Login-protected pages may not be accessible.
- Dynamically generated routes may require browser exploration.
- Sitemap availability depends on the website configuration.
- Do not bypass authentication or access restrictions.

## 7. Recommended MCP Usage

| MCP | Purpose |
|-----|---|
| Firecrawl | Discover and crawl website pages |
| Playwright | Explore buttons, forms and workflows |
| Browser Use | Perform complex browser interactions |
| Chrome DevTools | Inspect APIs and network requests |
| Apify | Extract structured website data |
| Tavily | Research websites and technologies |


## 8. Expected Deliverable

File: `website-sitemap.md`

The file should contain:
- Website overview
- Total discovered URLs
- Categorized URL inventory
- Duplicate URL information
- Sitemap information
- Discovery limitations



## 9. Recommended Workflow

Firecrawl Map
    ↓
Discover Website URLs
    ↓
Categorize Pages
    ↓
Firecrawl Crawl
    ↓
Extract Page Content
    ↓
Playwright Functionality Investigation
    ↓
Chrome DevTools API Investigation
    ↓
Final Website Investigation Report








"""






