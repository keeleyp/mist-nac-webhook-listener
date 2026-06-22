# Mist NAC Accounting Webhook Listener

Listens on port 8001 for Juniper Mist `nac-accounting` webhooks and appends
`NAC_ACCOUNTING_START`, `NAC_ACCOUNTING_UPDATE`, and `NAC_ACCOUNTING_STOP`
events to a dated CSV file (`mist_nac_YYYY-MM-DD.csv`). A new file is
created automatically when the date rolls over.

No third-party libraries required — only the Python standard library.

## Quick start

```bash
# 1. Clone
git clone https://github.com/keeleyp/mist-nac-webhook-listener.git
cd mist-nac-webhook-listener

# 2. Run (no install step needed)
python3 webhook_listener.py
```

## Configuration

Edit the constants at the top of `webhook_listener.py`:

| Variable | Default | Description |
|---|---|---|
| `PORT` | `8001` | TCP port to listen on |
| `DEBUG` | `True` | Print event summaries to stdout |
| `OUTPUT_DIR` | `"."` | Directory for CSV output files |

## Testing

With the listener running, send sample events:

```bash
python3 test_webhook.py
```

## Mist webhook setup

In the Mist portal: **Organization → Settings → Webhooks → Add Webhook**

- URL: `http://<your-server-ip>:8001/`
- Topics: `nac-accounting`
