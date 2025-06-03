"""
{# Cache and reuse metadata to avoid unnecessary gogdb.org requests #}
{%
    set metadata = gog_metadata(cookiecutter.gog_product_id)
%}
{{
    cookiecutter.update({
        "game_title": metadata.title,
        "pkgver": metadata.dl_installer
            | selectattr("os", "equalto", "linux")
            | first
            | attr("version"),
    })
}}
"""
