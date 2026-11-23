"""



# Website Intelligence – MCP Servers Notes

## Objective
Use Claude Code with MCP servers to extract complete information about a website, including:
- Website features and functionalities.
- All available pages and modules.
- Frontend and backend technologies.
- Database technology indicators.
- Third-party API integrations.
- API endpoints and HTTP methods.
- Website architecture.
- Hosting and infrastructure.
- Security observations.

---

## 1. Playwright MCP

**Purpose:** Browser automation and website feature discovery.

**Key Capabilities:**
- Navigate website pages.
- Click buttons and interact with elements.
- Fill and submit forms.
- Discover user workflows.
- Capture screenshots.
- Test dynamic website functionality.

**GitHub:** https://github.com/microsoft/playwright-mcp

---

## 2. Firecrawl MCP

**Purpose:** Website crawling and content extraction.

**Key Capabilities:**
- Crawl multiple website pages.
- Discover internal links.
- Extract page content.
- Convert website content into Markdown.
- Scrape JavaScript-rendered pages.
- Generate website page inventories.

**GitHub:** https://github.com/firecrawl/firecrawl-mcp-server

---

## 3. Chrome DevTools MCP

**Purpose:** Browser network and technical investigation.

**Key Capabilities:**
- Inspect network requests.
- Identify frontend API calls.
- Observe HTTP methods.
- Inspect request and response information.
- Read browser console errors.
- Analyze JavaScript execution.
- Investigate website performance.

**GitHub:** https://github.com/ChromeDevTools/chrome-devtools-mcp

---

## 4. Apify MCP

**Purpose:** Large-scale website data extraction.

**Key Capabilities:**
- Run website scrapers.
- Extract structured website data.
- Automate data collection.
- Use specialized scraping Actors.
- Support large-scale research.

**Website:** https://apify.com/

**GitHub:** https://github.com/apify/actors-mcp-server

---

## 5. Tavily MCP

**Purpose:** Internet research and website investigation.

**Key Capabilities:**
- Search the internet.
- Extract website information.
- Map website URLs.
- Crawl pages.
- Research third-party technologies.
- Find technical documentation.

**Website:** https://tavily.com/

---

## 6. Browser Use

**Purpose:** AI-powered browser automation.

**Key Capabilities:**
- Automate browser interactions.
- Investigate complex user journeys.
- Navigate dynamic interfaces.
- Automate multi-step workflows.

**GitHub:** https://github.com/browser-use/browser-use

---

## 7. Bright Data MCP

**Purpose:** Web data extraction at scale.

**Key Capabilities:**
- Extract public web data.
- Scrape websites.
- Collect structured information.
- Support large-scale research.

**Website:** https://brightdata.com/

---

## 8. Wappalyzer (Technology Detection API)

**Purpose:** Identify technologies used by websites.

**Key Capabilities:**
- Detect React, Next.js, Vue and Angular.
- Identify CMS platforms.
- Detect analytics technologies.
- Identify payment technology indicators.
- Detect JavaScript libraries.
- Identify hosting and CDN indicators.

**API Documentation:**
https://www.wappalyzer.com/docs/api/v2/lookup/

**Note:** Wappalyzer is a technology detection service, not necessarily an MCP server. Its API can be integrated into a custom MCP server.



---

# Recommended MCP Installation Priority

| Priority | MCP / Tool | Main Responsibility |
|---|---|---|
| 1 | Playwright | Feature and workflow discovery |
| 2 | Firecrawl | Website crawling |
| 3 | Chrome DevTools | API and network investigation |
| 4 | Wappalyzer API | Technology detection |

| 5 | Apify | Large-scale extraction |
| 6 | Tavily | Web research |
| 7 | Browser Use | Browser automation |
| 8 | Bright Data | Web data extraction |



3. Which MCP should handle which task?
Investigation task                     	Recommended MCP
Discover all website pages	            Firecrawl
Extract website content	                Firecrawl / Apify
Explore buttons and forms	            Playwright
Perform complex workflows	            Browser Use
Inspect API requests	                Chrome DevTools
Identify external APIs	                Chrome DevTools
Research technology documentation	    Tavily
Extract large-scale structured data	    Apify




| 2 | Firecrawl | Website crawling | Website crawling means automatically visiting a website's pages and discovering 
                                     all accessible internal links to understand the website's complete structure and content.

eg:  About Us: /about
     Services: /services
     Contact: /contact
     Pricing: /pricing


---

# Recommended Initial MCP Stack

Start with these four:

1. Playwright MCP.
2. Firecrawl MCP.
3. Chrome DevTools MCP.
4. Wappalyzer API.

Add other tools when required.

---

# Expected Final Deliverables

Claude should generate:

1. Complete website overview.
2. Feature and functionality inventory.
3. Page and route inventory.
4. Frontend technology report.
5. Backend technology report.
6. Database technology observations.
7. API inventory.
8. Third-party integration report.
9. Architecture documentation.
10. Security observations.
11. Technical recommendations.

## Important Investigation Rules

- Never fabricate missing information.
- Include evidence for important findings.
- Classify findings as Verified, Observed, Inferred or Unknown.
- Include confidence levels.
- Do not assume that an API exists without evidence.
- Respect authentication and authorization.
- Perform only authorized and non-invasive security checks.

**Final Goal:** Build a reusable Website Intelligence system using Claude Code and MCP servers that can investigate websites and produce professional A–Z technical documentation.










---

# Website Investigation Checklist

## A. Website Overview
- Website purpose.
- Business model.
- Industry.
- Main services.

## B. Page Inventory
- Homepage.
- Login and registration.
- Dashboard.
- Admin panel.
- User panel.
- Other accessible pages.

## C. Feature Analysis
- Website modules.
- Forms.
- Search functionality.
- Filters.
- Reports.
- Dashboards.
- Notifications.
- User workflows.

## D. Technology Stack
- Frontend framework.
- Backend framework.
- Programming languages.
- CSS framework.
- UI libraries.
- Database indicators.
- Build tools.
- Hosting.
- CDN.

## E. API Investigation
- Observed API endpoints.
- HTTP methods.
- Request headers.
- Content types.
- Response structures.
- Third-party API integrations.
- Authentication mechanisms.

## F. Third-Party Integrations
- Payment gateways.
- SMS providers.
- Email services.
- WhatsApp integrations.
- Google Maps.
- Authentication providers.
- Analytics platforms.
- Cloud storage.

## G. Architecture Analysis
- Frontend architecture.
- Backend architecture.
- API communication.
- Authentication flow.
- Third-party integration flow.
- Infrastructure observations.

## H. Security Analysis
- Security headers.
- Publicly exposed configuration.
- Exposed credentials.
- Authentication observations.
- Potential misconfigurations.









"""