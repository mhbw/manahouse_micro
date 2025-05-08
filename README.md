# The Mana House

**The Mana House** is a microservice and CLI tool that helps you match, enrich, and convert Magic: The Gathering card exports between platforms like ManaBox, TCGPlayer, Cardsphere, and Card Kingdom.

Powered by the [Scryfall API](https://scryfall.com/docs/api), [MTGJSON](https://mtgjson.com/), and a local SKU lookup system for accurate TCGPlayer exports.

---

## Features

- Parse card exports from ManaBox (more to come)
- Enrich cards with official Scryfall data and market prices
- Attach TCGPlayer SKU IDs using MTGJSON
- Export TCGPlayer-compatible CSVs with correct condition + finish mapping
- CLI-powered and Codespace-ready

---

## Quickstart (Locally)

```bash
# Clone the repo
git clone https://github.com/yourusername/mana-house.git
cd mana-house

# Install dependencies
pip install -e .

# Run CLI
mana-house convert manabox.csv --to tcgplayer --out tcg_upload.csv
