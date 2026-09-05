# dermocare — GitHub Project (classic) dashboard blueprint

## Limitation encountered

In this environment, available GitHub tooling is read-focused and does not expose a write operation to create **Projects (classic)** boards/cards directly.  
Because of that, this file provides the closest supported setup: a complete board blueprint you can copy into a classic project named `dermocare`.

## Team members

- diego — Data Engineer
- laura — Power BI Analyst
- marcos — Data Engineer
- ana — Power BI Analyst

## Suggested classic project workflow columns

1. Todo
2. In Progress
3. Review
4. Done

## Cards by status (preserving priority + assignee metadata)

### Todo

- **Define project KPIs**  
  Priority: **HIGH** · Assignee: **laura** (Power BI Analyst)  
  PM and analysts define KPIs for sales, inventory and margin.
- **Request access to POS API**  
  Priority: **HIGH** · Assignee: **diego** (Data Engineer)  
  Data Engineer requests credentials and tests connectivity.
- **Document data sources**  
  Priority: **MEDIUM** · Assignee: **marcos** (Data Engineer)  
  List POS, ERP and inventory systems with fields and update frequency.

### In Progress

- **Build ingestion pipeline for daily sales**  
  Priority: **HIGH** · Assignee: **marcos** (Data Engineer)  
  Create ingestion pipeline from POS API with retries and logging.
- **Clean and transform inventory data**  
  Priority: **MEDIUM** · Assignee: **diego** (Data Engineer)  
  Standardize product IDs, remove nulls and unify stock tables.
- **Create Power BI semantic model**  
  Priority: **HIGH** · Assignee: **laura** (Power BI Analyst)  
  Build model with fact_sales, dim_product and dim_store.
- **Draft dashboard layout**  
  Priority: **MEDIUM** · Assignee: **ana** (Power BI Analyst)  
  Create initial layout for sales and inventory dashboard.

### Review

- **Validate DAX measures**  
  Priority: **HIGH** · Assignee: **ana** (Power BI Analyst)  
  Check Sales, Margin, Out-of-Stock and Returns measures.
- **Review pipeline performance**  
  Priority: **MEDIUM** · Assignee: **marcos** (Data Engineer)  
  Test ingestion pipeline duration and resource usage.
- **Review dashboard layout with PM**  
  Priority: **LOW** · Assignee: **ana** (Power BI Analyst)  
  PM validates structure, navigation and visual hierarchy.

### Done

- **Project kickoff meeting**  
  Priority: **LOW** · Assignee: **diego** (Data Engineer)  
  PM and team align scope, roles and timelines.
- **Create repository structure**  
  Priority: **LOW** · Assignee: **marcos** (Data Engineer)  
  Initialize folders for pipelines, models and documentation.

## Optional metadata mapping inside classic projects

If you want to preserve metadata visually in classic cards:

- Prefix titles with priority: `[HIGH]`, `[MEDIUM]`, `[LOW]`
- Include assignee in card note body: `Assignee: @name`
- Add labels to linked issues (if using issue cards): `priority:high`, `priority:medium`, `priority:low`
