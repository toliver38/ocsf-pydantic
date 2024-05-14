# Project Name

OCSF-Pydantic

## Description

[Pydantic](https://docs.pydantic.dev/latest/) models for [OCSF schema](https://schema.ocsf.io) events and objects, for
validation and usage

## Installation

`pip install ocsf-pydantic`

## Usage

after install, the module & it's objects are available via `ocsf`

```
from ocsf.events.application.api import Api

apievent: dict = ... # an OCSF normalized dict
APIActivity(**apievent)

```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
