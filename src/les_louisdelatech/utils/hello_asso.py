BASE_URL = "https://api.helloasso.com/v5"


def get_orders(client, organization_slug: str, form_type: str, form_slug: str):
    results = []
    page_index = 1
    page_count = 1

    while page_index <= page_count:
        resp = client.get(
            f"{BASE_URL}/organizations/{organization_slug}/forms/{form_type}/{form_slug}/orders",
            params={
                "pageIndex": page_index,
                "pageSize": 100,
                "withDetails": True,
            },
        ).json()

        results += resp["data"]
        pagination = resp.get("pagination", {})
        page_count = pagination.get("totalPages", page_count)
        page_index += 1

    return results
