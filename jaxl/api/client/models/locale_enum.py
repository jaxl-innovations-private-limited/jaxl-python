"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum


class LocaleEnum(str, Enum):
    DE_ATGERMAN_AUSTRIA = "de-AT:German Austria"
    DE_CHGERMAN_SWITZERLAND = "de-CH:German Switzerland"
    DE_DEGERMAN_GERMANY = "de-DE:German Germany"
    EN_AUENGLISH_AUSTRALIA = "en-AU:English Australia"
    EN_CAENGLISH_CANADA = "en-CA:English Canada"
    EN_GBENGLISH_UNITED_KINGDOM = "en-GB:English United Kingdom"
    EN_HKENGLISH_HONG_KONG = "en-HK:English Hong Kong"
    EN_IEENGLISH_IRELAND = "en-IE:English Ireland"
    EN_INENGLISH_INDIA = "en-IN:English India"
    EN_NZENGLISH_NEW_ZEALAND = "en-NZ:English New Zealand"
    EN_PKENGLISH_PAKISTAN = "en-PK:English Pakistan"
    EN_USENGLISH_UNITED_STATES = "en-US:English United States"
    ES_ESSPANISH_SPAIN = "es-ES:Spanish Spain"
    ES_USSPANISH_UNITED_STATES = "es-US:Spanish United States"
    FR_BEFRENCH_BELGIUM = "fr-BE:French Belgium"
    FR_CAFRENCH_CANADA = "fr-CA:French Canada"
    FR_CHFRENCH_SWITZERLAND = "fr-CH:French Switzerland"
    FR_FRFRENCH_FRANCE = "fr-FR:French France"
    HI_INHINDI_INDIA = "hi-IN:Hindi India"
    IT_CHITALIAN_SWITZERLAND = "it-CH:Italian Switzerland"
    IT_ITITALIAN_ITALY = "it-IT:Italian Italy"
    JA_JPJAPANESE_JAPAN = "ja-JP:Japanese Japan"
    KO_KRKOREAN_SOUTH_KOREA = "ko-KR:Korean South Korea"
    NL_BEDUTCH_BELGIUM = "nl-BE:Dutch Belgium"
    NL_NLDUTCH_NETHERLANDS = "nl-NL:Dutch Netherlands"
    PT_BRPORTUGUESE_BRAZIL = "pt-BR:Portuguese Brazil"
    PT_PTPORTUGUESE_PORTUGAL = "pt-PT:Portuguese Portugal"

    def __str__(self) -> str:
        return str(self.value)
