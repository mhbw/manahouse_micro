import click
from parsers.manabox import parse_manabox_csv
from processor.enrich_and_price import enrich_and_price_cards
from exporter.csv_exporter import export_cards_to_tcgplayer_csv, export_cards_to_csv

@click.group()
def cli():
    pass

@cli.command()
@click.argument("input_csv", type=click.Path(exists=True))
@click.option("--to", type=click.Choice(["tcgplayer"]), required=True, help="Target export format")
@click.option("--out", type=click.Path(), default="enriched_output.csv", help="Path to output CSV")
@click.option("--sku-db", type=click.Path(), default="data/tcgplayer_skus.db", help="Path to TCGPlayer SKU database")
@click.option("--delay", type=float, default=0.2, help="Delay between Scryfall calls (seconds)")
def convert(input_csv, to, out, sku_db, delay):
    cards = parse_manabox_csv(input_csv)
    enriched, failed = enrich_and_price_cards(cards, delay=delay, sku_db_path=sku_db)

    if to == "tcgplayer":
        export_cards_to_tcgplayer_csv(enriched, out)

    if failed:
        failed_path = out.replace(".csv", "_failed.csv")
        export_cards_to_csv(failed, failed_path)

    print(f"[DONE] Converted {len(cards)} cards ({len(failed)} failed)")

if __name__ == "__main__":
    cli()
