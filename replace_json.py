from pathlib import Path
from src.logger import Logger
from src.config import Config
from src.excel_reader import ExcelReader
from src.json_reader import JsonReader
from src.mapping_engine import MappingEngine
from src.report_generator import ReportGenerator

PROJECT_ROOT = Path(__file__).resolve().parent


def main():

    logger = Logger(PROJECT_ROOT)

    logger.info("=" * 80)
    logger.info("JSON Replace Utility Started")
    logger.info("=" * 80)

    config = Config(PROJECT_ROOT)

    excel = ExcelReader(
        PROJECT_ROOT / "input" / "OBMDataInput.xlsx",
        logger
    )

    json_reader = JsonReader(
        PROJECT_ROOT / "input" / "input.json",
        logger
    )

    json_data = json_reader.load()

    excel_data = excel.load()

    engine = MappingEngine(
        json_data=json_data,
        excel_data=excel_data,
        config=config,
        logger=logger
    )

    updated_json = engine.execute()

    output = PROJECT_ROOT / "output" / "updated.json"

    json_reader.save(updated_json, output)

    report = ReportGenerator(
        engine.statistics,
        PROJECT_ROOT,
        logger
    )

    report.generate()

    logger.success("Completed Successfully")


if __name__ == "__main__":
    main()
