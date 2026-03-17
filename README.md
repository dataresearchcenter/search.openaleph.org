# search.openaleph.org

Editorial content for the [OpenAleph](https://search.openaleph.org) home page: highlight topics ("In the News") and curated dataset groups.

## Structure

- `topics.yml` — Highlight topics with images, search terms and collection references
- `dataset_groups.yml` — Curated dataset groups with collection IDs
- `build.py` — Transforms YAML sources into JSON for the frontend
- `dist/` — Built JSON files (git-ignored, deployed to S3)

## Usage

```bash
pip install -r requirements.txt
python build.py
```

This produces `dist/topics.json` and `dist/dataset_groups.json`.

## Deployment

Push the `main` branch or manually trigger the **Deploy** workflow in GitHub Actions. This builds the JSON and uploads to:

- `s3://cdn.investigativedata.org/search.openaleph.org/topics.json`
- `s3://cdn.investigativedata.org/search.openaleph.org/dataset_groups.json`

The frontend fetches these URLs via the `HighlightTopics` and `DatasetGroups` components.
