# Mist NAC Accounting Webhook Listener

Listens on port 8001 for Juniper Mist `nac-accounting` webhooks and appends
`NAC_ACCOUNTING_START`, `NAC_ACCOUNTING_UPDATE`, and `NAC_ACCOUNTING_STOP`
events to a dated Excel file (`mist_nac_YYYY-MM-DD.xlsx`). A new file is
created automatically when the date rolls over.

## Quick start

```bash
# 1. Clone
git clone https://github.com/keeleyp/mist-nac-webhook-listener.git
cd mist-nac-webhook-listener

# 2. Create venv and install dependencies (works on Debian/Raspberry Pi too)
bash setup.sh

# 3. Run
venv/bin/python3 webhook_listener.py
```

## Configuration

Edit the constants at the top of `webhook_listener.py`:

| Variable | Default | Description |
|---|---|---|
| `PORT` | `8001` | TCP port to listen on |
| `DEBUG` | `True` | Print event summaries to stdout |
| `OUTPUT_DIR` | `"."` | Directory for Excel output files |

## Testing

With the listener running, send sample events:

```bash
venv/bin/python3 test_webhook.py
```

## Mist webhook setup

In the Mist portal: **Organization → Webhooks → Add Webhook**

- URL: `http://<your-server-ip>:8001/`
- Topics: `nac-accounting`
