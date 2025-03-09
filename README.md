# cookiecutter-gog-pkgbuild

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for Arch Linux PKGBUILDs that package [GOG](https://www.gog.com) games.

## Using cookiecutter-gog-pkgbuild

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```bash
cookiecutter gh:claui/cookiecutter-gog-pkgbuild
```

### Alternative usage

If you use `cookiecutter-gog-pkgbuild` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```bash
abbreviations:
    gog-pkgbuild: https://github.com/claui/cookiecutter-gog-pkgbuild.git
```

Then, to generate a project, run:

```bash
cookiecutter gog-pkgbuild
```

## See also

- [cookiecutter-pkgbuild](https://github.com/claui/cookiecutter-pkgbuild)

## License

Copyright (c) 2021 – 2025 Claudia Pellegrino <clau@tiqua.de>

Licensed under the BSD Zero Clause License, see [LICENSE](LICENSE).
