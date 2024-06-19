def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report["./test_source_code_2.py"],
            "path": "./test_source_code_2.py",
            "status": "passed"
        },

        format_single_linter_file(
            list(linter_report.keys())[1],
            linter_report[list(linter_report.keys())[1]]
        ),

        format_single_linter_file(
            list(linter_report.keys())[2],
            linter_report[list(linter_report.keys())[2]]
        ),

        format_single_linter_file(
            list(linter_report.keys())[3],
            linter_report[list(linter_report.keys())[3]]
        )
    ]
