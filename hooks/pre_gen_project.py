# SPDX-FileCopyrightText: Claudia Pellegrino
# SPDX-License-Identifier: 0BSD

"""
{# Cache and reuse metadata to avoid unnecessary gogdb.org requests #}
{%
    set metadata = gog_metadata(cookiecutter.gog_product_id)
%}
{{
    cookiecutter.update({
        "game_title": metadata.title,
        "pkgver": metadata.dl_installer
            | selectattr("os", "equalto", cookiecutter.os)
            | first
            | attr("version"),
        "installer": metadata.dl_installer
            | selectattr("os", "equalto", cookiecutter.os)
            | first
            | attr("files")
            | first
            | attr("id"),
    })
}}
"""
