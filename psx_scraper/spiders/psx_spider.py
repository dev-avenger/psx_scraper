import scrapy
import re
import scrapy
import mysql.connector



class PsxSpiderSpider(scrapy.Spider):
    name = "psx_spider"
    allowed_domains = ["dps.psx.com.pk"]
    start_urls = ["https://dps.psx.com.pk"]
    base_url = "https://dps.psx.com.pk/company/"

    # Define an array of stock symbols to crawl
    # stock_symbols = ['PRL','ENGRO','NETSOL']
    stock_symbols = [
    "786",
    "AABS",
    "ABL",
    "ABOT",
    "ACIETF",
    "ACPL",
    "ADAMS",
    "ADMM",
    "AEL",
    "AGHA",
    "AGIC",
    "AGIL",
    "AGL",
    "AGLNCPS",
    "AGP",
    "AGSML",
    "AGTL",
    "AHCL",
    "AHL",
    "AHTM",
    "AICL",
    "AIRLINK",
    "AKBL",
    "AKDHL",
    "AKDSL",
    "AKGL",
    "ALAC",
    "ALIFE",
    "ALNRS",
    "ALTN",
    "AMBL",
    "ANL",
    "ANLNV",
    "ANTM",
    "APL",
    "ARCTM",
    "ARM",
    "ARPAK",
    "ARPL",
    "ARUJ",
    "ASC",
    "ASHT",
    "ASIC",
    "ASL",
    "ASLCPS",
    "ASLPS",
    "ASTL",
    "ASTM",
    "ATBA",
    "ATIL",
    "ATLH",
    "ATRL",
    "AVN",
    "AWTX",
    "BAFL",
    "BAFS",
    "BAHL",
    "BAPL",
    "BATA",
    "BCL",
    "BECO",
    "BERG",
    "BFMOD",
    "BGL",
    "BHAT",
    "BIFO",
    "BILF",
    "BIPL",
    "BNL",
    "BNWM",
    "BOK",
    "BOP",
    "BPL",
    "BRRG",
    "BTL",
    "BUXL",
    "BWCL",
    "BWHL",
    "CASH",
    "CCM",
    "CENI",
    "CEPB",
    "CFL",
    "CHAS",
    "CHCC",
    "CLOV",
    "CLVL",
    "CNERGY",
    "COLG",
    "CPHL",
    "CPPL",
    "CRTM",
    "CSAP",
    "CSIL",
    "CTM",
    "CWSM",
    "CYAN",
    "DAAG",
    "DADX",
    "DAWH",
    "DCL",
    "DCR",
    "DEL",
    "DFML",
    "DFSM",
    "DGKC",
    "DIIL",
    "DINT",
    "DLL",
    "DMTX",
    "DNCC",
    "DOL",
    "DSIL",
    "DSL",
    "DSML",
    "DWSM",
    "DWTM",
    "DYNO",
    "ECOP",
    "EFERT",
    "EFGH",
    "EFUG",
    "EFUL",
    "ELCM",
    "ELSM",
    "EMCO",
    "ENGRO",
    "EPCL",
    "EPCLPS",
    "EPQL",
    "ESBL",
    "EWIC",
    "EXIDE",
    "FABL",
    "FANM",
    "FASM",
    "FATIMA",
    "FCCL",
    "FCEPL",
    "FCIBL",
    "FCSC",
    "FDIBL",
    "FECM",
    "FECTC",
    "FEM",
    "FEROZ",
    "FFBL",
    "FFC",
    "FFL",
    "FFLM",
    "FHAM",
    "FIBLM",
    "FIMM",
    "FLYNG",
    "FML",
    "FNEL",
    "FPJM",
    "FPRM",
    "FRCL",
    "FRSM",
    "FTMM",
    "FTSM",
    "FUDLM",
    "FZCM",
    "GADT",
    "GAL",
    "GAMON",
    "GATI",
    "GATM",
    "GCIL",
    "GEMPAPL",
    "GEMSPNL",
    "GEMUNSL",
    "GFIL",
    "GGGL",
    "GGL",
    "GHGL",
    "GHNI",
    "GIL",
    "GLAXO",
    "GLPL",
    "GOC",
    "GRR",
    "GRYL",
    "GTYR",
    "GVGL",
    "GWLC",
    "HABSM",
    "HAEL",
    "HAFL",
    "HALEON",
    "HASCOL",
    "HBL",
    "HBLTETF",
    "HCAR",
    "HCL",
    "HGFA",
    "HICL",
    "HIFA",
    "HINO",
    "HINOON",
    "HIRAT",
    "HMB",
    "HPL",
    "HRPL",
    "HTL",
    "HUBC",
    "HUMNL",
    "HUSI",
    "HWQS",
    "IBFL",
    "IBLHL",
    "ICIBL",
    "ICL",
    "IDRT",
    "IDSM",
    "IDYM",
    "IGIHL",
    "IGIL",
    "ILP",
    "IMAGE",
    "IML",
    "INDU",
    "INIL",
    "INKL",
    "ISIL",
    "ISL",
    "ITTEFAQ",
    "JATM",
    "JDMT",
    "JDWS",
    "JGICL",
    "JKSM",
    "JLICL",
    "JOPP",
    "JSBL",
    "JSCL",
    "JSCLPSA",
    "JSGBETF",
    "JSGCL",
    "JSIL",
    "JSMFETF",
    "JSML",
    "JUBS",
    "JVDC",
    "JVDCPS",
    "KAPCO",
    "KCL",
    "KEL",
    "KHTC",
    "KHYT",
    "KML",
    "KOHC",
    "KOHE",
    "KOHP",
    "KOHTM",
    "KOIL",
    "KOSM",
    "KPUS",
    "KSBP",
    "KTML",
    "LCI",
    "LEUL",
    "LMSM",
    "LOADS",
    "LOTCHEM",
    "LPGL",
    "LPL",
    "LSEPL",
    "LSEVL",
    "LUCK",
    "MACFL",
    "MACTER",
    "MARI",
    "MCB",
    "MCBIM",
    "MDTL",
    "MEBL",
    "MEHT",
    "MERIT",
    "META",
    "MFFL",
    "MFL",
    "MIRKS",
    "MLCF",
    "MODAM",
    "MQTM",
    "MRNS",
    "MSCL",
    "MSOT",
    "MSOTPS",
    "MTL",
    "MUGHAL",
    "MUREB",
    "MZNPETF",
    "NAGC",
    "NATF",
    "NATM",
    "NBP",
    "NBPGETF",
    "NCL",
    "NCML",
    "NCPL",
    "NESTLE",
    "NETSOL",
    "NEXT",
    "NICL",
    "NITGETF",
    "NML",
    "NONS",
    "NPL",
    "NRL",
    "NRSL",
    "NSRM",
    "OBOY",
    "OCTOPUS",
    "OGDC",
    "OLPL",
    "OLPM",
    "OML",
    "ORM",
    "OTSU",
    "PABC",
    "PACE",
    "PAEL",
    "PAKD",
    "PAKL",
    "PAKOXY",
    "PAKRI",
    "PAKT",
    "PASL",
    "PCAL",
    "PECO",
    "PELPS",
    "PGLC",
    "PHDL",
    "PIAA",
    "PIAB",
    "PIBTL",
    "PICT",
    "PIL",
    "PIM",
    "PINL",
    "PIOC",
    "PKGI",
    "PKGP",
    "PKGS",
    "PMI",
    "PMPK",
    "PMRS",
    "PNSC",
    "POL",
    "POML",
    "POWER",
    "POWERPS",
    "PPL",
    "PPP",
    "PPVC",
    "PREMA",
    "PRET",
    "PRL",
    "PRWM",
    "PSEL",
    "PSMC",
    "PSO",
    "PSX",
    "PSYL",
    "PTC",
    "PTL",
    "QUET",
    "QUICE",
    "RCML",
    "REDCO",
    "REWM",
    "RICL",
    "RMPL",
    "RPL",
    "RUBY",
    "RUPL",
    "SAIF",
    "SANSM",
    "SAPT",
    "SARC",
    "SASML",
    "SAZEW",
    "SBL",
    "SCBPL",
    "SCL",
    "SEARL",
    "SEL",
    "SEPL",
    "SERT",
    "SFL",
    "SGABL",
    "SGF",
    "SGPL",
    "SHCM",
    "SHDT",
    "SHEL",
    "SHEZ",
    "SHFA",
    "SHJS",
    "SHNI",
    "SHSML",
    "SIBL",
    "SIEM",
    "SILK",
    "SINDM",
    "SITC",
    "SKRS",
    "SLL",
    "SMBL",
    "SMCPL",
    "SML",
    "SNAI",
    "SNBL",
    "SNGP",
    "SPEL",
    "SPL",
    "SPWL",
    "SRVI",
    "SSGC",
    "SSML",
    "SSOM",
    "STCL",
    "STJT",
    "STML",
    "STPL",
    "SUHJ",
    "SURC",
    "SUTM",
    "SYM",
    "SYS",
    "SZTM",
    "TATM",
    "TCORP",
    "TCORPCPS",
    "TELE",
    "TGL",
    "THALL",
    "THCCL",
    "TICL",
    "TOMCL",
    "TOWL",
    "TPL",
    "TPLI",
    "TPLP",
    "TPLT",
    "TREET",
    "TRG",
    "TRIPF",
    "TRSM",
    "TSBL",
    "TSMF",
    "TSML",
    "TSPL",
    "UBDL",
    "UBL",
    "UBLPETF",
    "UCAPM",
    "UDPL",
    "UNIC",
    "UNITY",
    "UPFL",
    "UVIC",
    "WAHN",
    "WAVES",
    "WHALE",
    "WTL",
    "YOUW",
    "ZAHID",
    "ZIL",
    "ZTL"
]
#     stock_symbols = [
#     "KOSM",
#     "PRL",
#     "TPLP",
#     "PIBTL",
#     "WTL",
#     "CNERGY",
#     "AIRLINK",
#     "SEARL",
#     "UNITY",
#     "KEL",
#     "HUMNL",
#     "SNGP",
#     "FFL",
#     "GGL",
#     "OGDC",
#     "ASC",
#     "YOUW",
#     "TELE",
#     "FCCL",
#     "PAEL",
#     "BIPL",
#     "PPL",
#     "GATM",
#     "MEBL",
#     "AGL",
#     "MLCF",
#     "NML",
#     "BOP",
#     "CPHL",
#     "DGKC",
#     "FABL",
#     "DCL",
#     "HUBC",
#     "BAFL",
#     "TRG",
#     "TREET",
#     "CEPB",
#     "JSBL",
#     "PABC",
#     "SSGC",
#     "AICL",
#     "HASCOL",
#     "PSO",
#     "GCIL",
#     "SYM",
#     "IMAGE",
#     "ASL",
#     "PICT",
#     "KAPCO",
#     "ILP",
#     "DFML",
#     "DOL",
#     "GHGL",
#     "FLYNG",
#     "SILK",
#     "AVN",
#     "SAZEW",
#     "WAVES",
#     "ASTL",
#     "RPL",
#     "AGHA",
#     "ANL",
#     "SHEL",
#     "TOMCL",
#     "NRL",
#     "ATRL",
#     "POWER",
#     "EPCL",
#     "PTL",
#     "NCPL",
#     "MUGHAL",
#     "TPL",
#     "FFBL",
#     "GTYR",
#     "HIFA",
#     "MFL",
#     "NPL",
#     "ISL",
#     "HCAR",
#     "GGGL",
#     "NBP",
#     "AGP",
#     "PACE",
#     "TGL",
#     "LPL",
#     "GHNI",
#     "GAL",
#     "NETSOL",
#     "PSX",
#     "LOADS",
#     "UBL",
#     "WHALE",
#     "NCL",
#     "INIL",
#     "HBL",
#     "EPQL",
#     "PTC",
#     "JSCL",
#     "PIAA",
#     "CHCC",
#     "PIOC",
#     "HTL",
#     "PREMA",
#     "OCTOPUS",
#     "LUCK",
#     "ENGRO",
#     "ALTN",
#     "SGF",
#     "STPL",
#     "BGL",
#     "OLPL",
#     "LOTCHEM",
#     "SPWL",
#     "SYS",
#     "ITTEFAQ",
#     "STCL",
#     "EFERT",
#     "KOIL",
#     "FFC",
#     "PAKRI",
#     "FCEPL",
#     "FNEL",
#     "FEROZ",
#     "LSEVL",
#     "TSPL",
#     "DSL",
#     "IBLHL",
#     "MCB",
#     "SMBL",
#     "PASL",
#     "GLAXO",
#     "MODAM",
#     "THCCL",
#     "TCORP",
#     "MERIT",
#     "CSAP",
#     "DCR",
#     "DSIL",
#     "ICL",
#     "POL",
#     "CTM",
#     "FCSC",
#     "SNBL",
#     "MDTL",
#     "DYNO",
#     "HMB",
#     "BNL",
#     "DFSM",
#     "FHAM",
#     "OBOY",
#     "HBLTETF",
#     "NATF",
#     "ACPL",
#     "MFFL",
#     "META",
#     "BECO",
#     "UBLPETF",
#     "HWQS",
#     "UNIC",
#     "GFIL",
#     "AKBL",
#     "QUICE",
#     "BAHL",
#     "PAKOXY",
#     "SPL",
#     "ICIBL",
#     "BERG",
#     "MACFL",
#     "GVGL",
#     "ATBA",
#     "MTL",
#     "HALEON",
#     "FDIBL",
#     "PMI",
#     "MARI",
#     "IDYM",
#     "MCBIM",
#     "MRNS",
#     "AGIL",
#     "GWLC",
#     "ADMM",
#     "JLICL",
#     "HINOON",
#     "PSMC",
#     "SHFA",
#     "CPPL",
#     "NRSL",
#     "ESBL",
#     "FPRM",
#     "SEL",
#     "PAKOXYR",
#     "FATIMA",
#     "KOHC",
#     "SPEL",
#     "AHL",
#     "SCBPL",
#     "TPLI",
#     "QUET",
#     "DNCC",
#     "BIFO",
#     "EFGH",
#     "DEL",
#     "OLPM",
#     "IGIHL",
#     "HIRAT",
#     "AHCL",
#     "CSIL",
#     "TRIPF",
#     "SKRS",
#     "HGFA",
#     "AGSML",
#     "JVDC",
#     "GRR",
#     "NICL",
#     "ALAC",
#     "IML",
#     "TOWL",
#     "CRTM",
#     "AGIC",
#     "PNSC",
#     "PKGP",
#     "KOHP",
#     "CYAN",
#     "KML",
#     "PKGS",
#     "SUTM",
#     "SEPL",
#     "ABL",
#     "OTSU",
#     "SHSML",
#     "LSEPL",
#     "KOHE",
#     "NCML",
#     "KSBP",
#     "DWSM",
#     "BILF",
#     "ALIFE",
#     "REDCO",
#     "ARPL",
#     "HUSI",
#     "WAHN",
#     "APL",
#     "BCL",
#     "MZNPETF",
#     "MIRKS",
#     "KTML",
#     "SINDM",
#     "PGLC",
#     "PCAL",
#     "TPLT",
#     "DAWH",
#     "AGTL",
#     "ABOT",
#     "ASTM",
#     "HABSM",
#     "HINO",
#     "KHTC",
#     "DLL",
#     "JSMFETF",
#     "PHDL",
#     "CLOV",
#     "CWSM",
#     "GAMON",
#     "RUPL",
#     "JSGBETF",
#     "SMCPL",
#     "SHEZ",
#     "SAIF",
#     "COLG",
#     "GADT",
#     "ZTL",
#     "HPL",
#     "PIL",
#     "PMPK",
#     "EXIDE",
#     "ECOP",
#     "BNWM",
#     "FUDLM",
#     "ASHT",
#     "MSOT",
#     "PPP",
#     "RUBY",
#     "BWCL",
#     "ARM",
#     "MUREB",
#     "INDU",
#     "IGIL",
#     "FECTC",
#     "SHDT",
#     "CENI",
#     "SERT",
#     "HAEL",
#     "786",
#     "NEXT",
#     "ATLH",
#     "PAKD",
#     "BUXL",
#     "UCAPM",
#     "JGICL",
#     "BRRG",
#     "ARCTM",
#     "TSBL",
#     "ADAMS",
#     "ATIL",
#     "AKDHL",
#     "ARUJ",
#     "TRSM",
#     "IBFL",
#     "SARC",
#     "FML",
#     "UVIC",
#     "JUBS",
#     "EFUG",
#     "EPCLPS",
#     "SRVI",
#     "BATA",
#     "PAKT",
#     "PINL",
#     "OML",
#     "HICL",
#     "CLVL",
#     "JSML",
#     "UDPL",
#     "SBL",
#     "AEL",
#     "NONS",
#     "STML",
#     "POML",
#     "JKSM",
#     "GLPL",
#     "FZCM",
#     "THALL",
#     "SIEM",
#     "GATI",
#     "AABS",
#     "PSYL",
#     "PAKL",
#     "PIM",
#     "TATM",
#     "JDMT",
#     "SGPL",
#     "BAPL",
#     "DADX",
#     "FPJM",
#     "NAGC",
#     "SITC",
#     "SML",
#     "SNAI",
#     "TSMF",
#     "SHNI",
#     "BPL",
#     "LEUL",
#     "STJT",
#     "LCI",
#     "NESTLE",
#     "SFL",
#     "PRET",
#     "EFUL",
#     "MEHT",
#     "TICL",
#     "JSGCL",
#     "RMPL",
#     "UPFL"
# ] # Add the symbols you want to crawl


    def start_requests(self):
        for stock_symbol in self.stock_symbols:
            # Generate the URL for each stock symbol
            url = f'{self.base_url}{stock_symbol}'
            print(url)
            yield scrapy.Request(url, callback=self.parse, meta={'symbol': stock_symbol})

    def parse(self, response):
        # Extract data using CSS query selectors
        symbol = response.meta['symbol']

        #Daily Information Start
        stock_price = response.css('div.quote__details > div.quote__price > div.quote__close::text').get()
        stock_price_change = response.css('div.quote__details > div.quote__price > div.quote__change.change__text--pos > div.change__value::text').get()
        stock_price_change_percentage = response.css('div.quote__details > div.quote__price > div.quote__change.change__text--pos > div.change__percent::text').get()

        open = response.css('div.stats.stats--noborder > div:nth-child(1) > div.stats_value::text').get()
        high = response.css('div.stats.stats--noborder > div:nth-child(2) > div.stats_value::text').get()
        low = response.css('div.stats.stats--noborder > div:nth-child(3) > div.stats_value::text').get()
        volume = response.css('div.stats.stats--noborder > div:nth-child(4) > div.stats_value::text').get()

        circuit_breaker = response.css('div.stats.company__quote__rangeStats > div:nth-child(1) > div.stats_value::text').get()
        day_range = response.css('div.stats.company__quote__rangeStats > div:nth-child(2) > div.stats_value::text').get()
        week_range_52 = response.css('div.stats.company__quote__rangeStats > div:nth-child(3) > div.stats_value::text').get()

        ldcp = response.css('div.tabs__panel.tabs__panel > div:nth-child(4) > div:nth-child(1) > div.stats_value::text').get()
        var = response.css('div.tabs__panel.tabs__panel > div:nth-child(4) > div:nth-child(2) > div.stats_value::text').get()
        haircut = response.css('div.tabs__panel.tabs__panel > div:nth-child(4) > div:nth-child(3) > div.stats_value::text').get()
        p_e_ratio_ttm = response.css('div.tabs__panel.tabs__panel > div:nth-child(4) > div:nth-child(4) > div.stats_value::text').get()


        one_year_change = response.css('div.tabs__panel.tabs__panel > div:nth-child(5) > div:nth-child(1) > div.stats_value.change__text--pos::text').get()
        ytd_change = response.css('div.tabs__panel.tabs__panel > div:nth-child(5) > div:nth-child(2) > div.stats_value.change__text--pos::text').get()

        #Daily Information End



        #Company Information Start
        company_name = response.css('div.quote__details > div.quote__name::text').get()
        company_website = response.css('#profile > div > div:nth-child(3) > div:nth-child(1) > p:nth-child(4) > a::text').get()
        company_fiscal_year_end = response.css('#profile > div > div:nth-child(3) > div:nth-child(3) > p:nth-child(4)::text').get()
        company_description = response.css('#profile > div > div:nth-child(2) > div.profile__item.profile__item--decription > p::text').get()
        company_address = response.css('#profile > div > div:nth-child(3) > div:nth-child(1) > p:nth-child(2)::text').get()
        company_registrar = response.css('#profile > div > div:nth-child(3) > div:nth-child(2) > p::text').get()
        company_auditor = response.css('#profile > div > div:nth-child(3) > div:nth-child(3) > p:nth-child(2)::text').get()
        #Company Information End


        #Equity Profile Start
        market_cap = response.css('#equity > div > div:nth-child(1) > div.stats_value::text').get()
        shares = response.css('#equity > div > div:nth-child(2) > div.stats_value::text').get()
        free_float = response.css('#equity > div > div:nth-child(3) > div.stats_value::text').get()
        free_float_percentage = response.css('#equity > div > div:nth-child(4) > div.stats_value::text').get()
        #Equity Profile End

        #Sector Information Start
        sector_name = response.css('div.quote__details > div.quote__sector > span::text').get()
        #Sector Information End

        #Financials Annual Start

        a_sales_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span::text').get()
        a_profit_after_taxation_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > span::text').get()
        a_eps_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > span::text').get()
        a_year_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > thead > tr > th:nth-child(2)::text').get()

        a_sales_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span::text').get()
        a_profit_after_taxation_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span::text').get()
        a_eps_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > span::text').get()
        a_year_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > thead > tr > th:nth-child(3)::text').get()


        a_sales_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > span::text').get()
        a_profit_after_taxation_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > span::text').get()
        a_eps_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > span::text').get()
        a_year_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > thead > tr > th:nth-child(4)::text').get()

        a_sales_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > span::text').get()
        a_profit_after_taxation_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > span::text').get()
        a_eps_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > span::text').get()
        a_year_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Annual"] > div > table > thead > tr > th:nth-child(5)::text').get()

        #Financials Annual End

        #Financials Quarterly Start

        q_sales_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span::text').get()
        q_profit_after_taxation_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > span::text').get()
        q_eps_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > span::text').get()
        q_year_1 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > thead > tr > th:nth-child(2)::text').get()

        q_sales_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span::text').get()
        q_profit_after_taxation_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span::text').get()
        q_eps_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > span::text').get()
        q_year_2 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > thead > tr > th:nth-child(3)::text').get()

        q_sales_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > span::text').get()
        q_profit_after_taxation_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > span::text').get()
        q_eps_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > span::text').get()
        q_year_3 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > thead > tr > th:nth-child(4)::text').get()


        q_sales_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > span::text').get()
        q_profit_after_taxation_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > span::text').get()
        q_eps_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > span::text').get()
        q_year_4 = response.css('#financialTab > div > div.tabs__panels > div.tabs__panel.tabs__panel[data-name="Quarterly"] > div > table > thead > tr > th:nth-child(5)::text').get()

        #Financials Quarterly End


        #Ratios Start

        gross_profit_margin_percentage_1 = response.css('#ratios > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span::text').get()
        net_profit_margin_percentage_1 = response.css('#ratios > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > span::text').get()
        eps_growth_percentage_1 = response.css('#ratios > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > span::text').get()
        peg_1 = response.css('#ratios > div > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > span::text').get()
        ratio_year_1 = response.css('#ratios > div > div > table > thead > tr > th:nth-child(2)::text').get()

        gross_profit_margin_percentage_2 = response.css('#ratios > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span::text').get()
        net_profit_margin_percentage_2 = response.css('#ratios > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span::text').get()
        eps_growth_percentage_2 = response.css('#ratios > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > span::text').get()
        peg_2 = response.css('#ratios > div > div > table > tbody > tr:nth-child(4) > td:nth-child(3) > span::text').get()
        ratio_year_2 = response.css('#ratios > div > div > table > thead > tr > th:nth-child(3)::text').get()

        gross_profit_margin_percentage_3 = response.css('#ratios > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > span::text').get()
        net_profit_margin_percentage_3 = response.css('#ratios > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > span::text').get()
        eps_growth_percentage_3 = response.css('#ratios > div > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > span::text').get()
        peg_3 = response.css('#ratios > div > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > span::text').get()
        ratio_year_3 = response.css('#ratios > div > div > table > thead > tr > th:nth-child(4)::text').get()

        gross_profit_margin_percentage_4 = response.css('#ratios > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > span::text').get()
        net_profit_margin_percentage_4 = response.css('#ratios > div > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > span::text').get()
        eps_growth_percentage_4 = response.css('#ratios > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > span::text').get()
        peg_4 = response.css('#ratios > div > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > span::text').get()
        ratio_year_4 = response.css('#ratios > div > div > table > thead > tr > th:nth-child(5)::text').get()


        #Ratios End

        #Formatting Daily Information Start
        formatted_price = stock_price.replace('Rs.', '') if stock_price else None

        formatted_price_change_percentage = stock_price_change_percentage.replace(' ', '').replace('%','') if stock_price_change_percentage else None
        formatted_volume = volume.replace(",", "") if volume else None

        formatted_one_year_change = one_year_change.strip('%').replace(' ', '') if one_year_change else None
        formatted_ytd_change = ytd_change.strip('%').replace(' ', '') if ytd_change else None

        circuit_breaker_split = circuit_breaker.split(" — ") if circuit_breaker else None
        lower_cap  = circuit_breaker_split[0] if circuit_breaker_split else None
        higher_cap = circuit_breaker_split[1] if circuit_breaker_split else None

        week_range_52_split = week_range_52.split(" — ") if week_range_52 else None
        week_lower_52 = week_range_52_split[0] if week_range_52_split else None
        week_higher_52 = week_range_52_split[1] if week_range_52_split else None

        a_eps_1_numeric = a_eps_1.replace(',','') if a_eps_1 else None
        formatted_a_eps_1 = self.convert_negative(a_eps_1_numeric) if a_eps_1_numeric else None

        pe_ratio = float(formatted_price) / float(formatted_a_eps_1) if formatted_a_eps_1 else None

        #Formatting Daily Information End

        #Formatting Equity Profile Start
        formatted_market_cap = market_cap.replace(',','') if market_cap else None
        formatted_shares = shares.replace(',','') if shares else None
        formatted_free_float = free_float.replace(',','') if free_float else None
        formatted_free_float_percentage = free_float_percentage.strip('%') if free_float_percentage else None

        #Formatting Equity Profile End

        #Formatted Financials Annual Start

        formatted_a_sales_1 = a_sales_1.replace(',','') if a_sales_1 else None
        formatted_a_profit_after_taxation_1 = a_profit_after_taxation_1.replace(',','') if a_profit_after_taxation_1 else None

        formatted_a_sales_2 = a_sales_2.replace(',', '') if a_sales_2 else None
        formatted_a_profit_after_taxation_2 = a_profit_after_taxation_2.replace(',','') if a_profit_after_taxation_2 else None

        formatted_a_sales_3 = a_sales_3.replace(',', '') if a_sales_3 else None
        formatted_a_profit_after_taxation_3 = a_profit_after_taxation_3.replace(',','') if a_profit_after_taxation_3 else None

        formatted_a_sales_4 = a_sales_4.replace(',', '') if a_sales_4 else None
        formatted_a_profit_after_taxation_4 = a_profit_after_taxation_4.replace(',','') if a_profit_after_taxation_4 else None

        #Formatted Financials Annual End

        #Formatted Financials Quarterly Start

        formatted_q_sales_1 = q_sales_1.replace(',','') if q_sales_1 else None
        formatted_q_profit_after_taxation_1 = q_profit_after_taxation_1.replace(',','') if q_profit_after_taxation_1 else None

        formatted_q_sales_2 = q_sales_2.replace(',','') if q_sales_2 else None
        formatted_q_profit_after_taxation_2 = q_profit_after_taxation_2.replace(',','') if q_profit_after_taxation_2 else None

        formatted_q_sales_3 = q_sales_3.replace(',','') if q_sales_3 else None
        formatted_q_profit_after_taxation_3 = q_profit_after_taxation_3.replace(',','') if q_profit_after_taxation_3 else None


        formatted_q_sales_4 = q_sales_4.replace(',','') if q_sales_4 else None
        formatted_q_profit_after_taxation_4 = q_profit_after_taxation_4.replace(',','') if q_profit_after_taxation_4 else None

        #Formatted Financials Quarterly End

        stock_data = {
            'symbol': symbol,
            'price': formatted_price,
            'change_value': self.convert_negative(stock_price_change),
            'change_percentage': self.convert_negative(formatted_price_change_percentage),
            'open_value': open,
            'high': high,
            'low': low,
            'volume': formatted_volume,
            'circuit_breaker': circuit_breaker,
            'lower_cap': lower_cap,
            'higher_cap': higher_cap,
            'day_range': day_range,
            'week_range_52': week_range_52,
            'week_lower_52': week_lower_52,
            'week_higher_52': week_higher_52,
            'sector': sector_name,
            'ldcp': ldcp,
            'var': var,
            'haircut': haircut,
            'pe_ratio_ttm': p_e_ratio_ttm,
            'one_year_change': formatted_one_year_change,
            'ytd_change': formatted_ytd_change,
            'pe_ratio': pe_ratio,
            '2023': self.convert_negative(a_eps_1),
            '2022': self.convert_negative(a_eps_2),
            '2021': self.convert_negative(a_eps_3),
            '2020': self.convert_negative(a_eps_4),
        }
        self.insert_into_mysql(stock_data)
        # stock_data = {
        #     symbol:{
        #         'daily':{
        #             'price':formatted_price,
        #             'change': stock_price_change,
        #             'change_percentage': formatted_price_change_percentage,
        #             'open': open,
        #             'high': high,
        #             'low': low,
        #             'volume': formatted_volume,
        #             'circuit_breaker': circuit_breaker,
        #             'lower_cap':lower_cap,
        #             'higher_cap':higher_cap,
        #             'day_range': day_range,
        #             'week_range_52': week_range_52,
        #             'week_lower_52': week_lower_52,
        #             'week_higher_52': week_higher_52,
        #             'ldcp': ldcp,
        #             'var': var,
        #             'haircut': haircut,
        #             'pe_ratio_ttm': p_e_ratio_ttm,
        #             'one_year_change': formatted_one_year_change,
        #             'ytd_change': formatted_ytd_change,
        #             'pe_ratio': pe_ratio
        #
        #         },
        #         'company':{
        #             'name':company_name,
        #             'website':company_website,
        #             'fiscal_year_end':company_fiscal_year_end,
        #             'description':company_description,
        #             'address': company_address,
        #             'registrar':company_registrar,
        #             'auditor':company_auditor
        #         },
        #         'equity':{
        #             'market_cap':formatted_market_cap,
        #             'shares':formatted_shares,
        #             'free_float':formatted_free_float,
        #             'free_float_percent':formatted_free_float_percentage
        #         },
        #         'sector':{
        #             'name':sector_name
        #         },
        #         'financials_annual':[
        #             {
        #                 'sales': self.convert_negative(formatted_a_sales_1),
        #                 'profit_after_taxation': self.convert_negative(formatted_a_profit_after_taxation_1),
        #                 'eps':self.convert_negative(a_eps_1),
        #                 'year':a_year_1
        #
        #             },
        #             {
        #                 'sales': self.convert_negative(formatted_a_sales_2),
        #                 'profit_after_taxation': self.convert_negative(formatted_a_profit_after_taxation_2),
        #                 'eps': self.convert_negative(a_eps_2),
        #                 'year': a_year_2
        #
        #             },
        #             {
        #                 'sales': self.convert_negative(formatted_a_sales_3),
        #                 'profit_after_taxation': self.convert_negative(formatted_a_profit_after_taxation_3),
        #                 'eps': self.convert_negative(a_eps_3),
        #                 'year': a_year_3
        #
        #             },
        #             {
        #                 'sales': self.convert_negative(formatted_a_sales_4),
        #                 'profit_after_taxation': self.convert_negative(formatted_a_profit_after_taxation_4),
        #                 'eps': self.convert_negative(a_eps_4),
        #                 'year': a_year_4
        #
        #             },
        #         ],
        #         'financials_quarterly': [
        #             {
        #                 'sales': self.convert_negative(formatted_q_sales_1),
        #                 'profit_after_taxation': self.convert_negative(formatted_q_profit_after_taxation_1),
        #                 'eps': self.convert_negative(q_eps_1),
        #                 'year': q_year_1
        #
        #             },
        #             {
        #                 'sales': self.convert_negative(formatted_q_sales_2),
        #                 'profit_after_taxation': self.convert_negative(formatted_q_profit_after_taxation_2),
        #                 'eps': self.convert_negative(q_eps_2),
        #                 'year': q_year_2
        #
        #             },
        #             {
        #                 'sales': self.convert_negative(formatted_q_sales_3),
        #                 'profit_after_taxation': self.convert_negative(formatted_q_profit_after_taxation_3),
        #                 'eps': self.convert_negative(q_eps_3),
        #                 'year': q_year_3
        #
        #             },
        #             {
        #                 'sales': self.convert_negative(formatted_q_sales_4),
        #                 'profit_after_taxation': self.convert_negative(formatted_q_profit_after_taxation_4),
        #                 'eps': self.convert_negative(q_eps_4),
        #                 'year': q_year_4
        #
        #             },
        #         ],
        #         'ratios': [
        #             {
        #                 'gross_profit_margin_percentage': self.convert_negative(gross_profit_margin_percentage_1),
        #                 'net_profit_margin_percentage': self.convert_negative(net_profit_margin_percentage_1),
        #                 'eps_growth_percentage': self.convert_negative(eps_growth_percentage_1),
        #                 'peg': self.convert_negative(peg_1),
        #                 'year':ratio_year_1
        #
        #             },
        #             {
        #                 'gross_profit_margin_percentage': self.convert_negative(gross_profit_margin_percentage_2),
        #                 'net_profit_margin_percentage': self.convert_negative(net_profit_margin_percentage_2),
        #                 'eps_growth_percentage': self.convert_negative(eps_growth_percentage_2),
        #                 'peg': self.convert_negative(peg_2),
        #                 'year': ratio_year_2
        #
        #             },
        #             {
        #                 'gross_profit_margin_percentage': self.convert_negative(gross_profit_margin_percentage_3),
        #                 'net_profit_margin_percentage': self.convert_negative(net_profit_margin_percentage_3),
        #                 'eps_growth_percentage': self.convert_negative(eps_growth_percentage_3),
        #                 'peg': self.convert_negative(peg_3),
        #                 'year':ratio_year_3
        #
        #             },
        #             {
        #                 'gross_profit_margin_percentage': self.convert_negative(gross_profit_margin_percentage_4),
        #                 'net_profit_margin_percentage': self.convert_negative(net_profit_margin_percentage_4),
        #                 'eps_growth_percentage': self.convert_negative(eps_growth_percentage_4),
        #                 'peg': self.convert_negative(peg_4),
        #                 'year':ratio_year_4
        #
        #             },
        #         ],
        #
        #     }
        #     # Add more fields as needed
        # }
        # print(stock_data)
        yield stock_data

    def convert_negative(self,text):
        if text is not None:
            if '(' in text and ')' in text:
                # Remove parentheses and convert to a negative number
                number = text.strip('()')
                negative_number = -float(number.replace(',',''))
                return negative_number
            else:
                # No parentheses, so keep the text as is
                return text
        else:
            return text


    def insert_into_mysql(self, stock_data):
        # Create a MySQL database connection
        try:

            conn = mysql.connector.connect(
                host='localhost',
                user='wsl_root',
                password='Password123@',
                database='psx_database'
            )

            cursor = conn.cursor()

            # Define the table schema
            create_table_query = """
            CREATE TABLE IF NOT EXISTS stock_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                symbol VARCHAR(255),
                price DECIMAL(10, 2),
                change_value DECIMAL(10, 2) SIGNED,
                change_percentage DECIMAL(10, 2) SIGNED,
                open_value DECIMAL(10, 2),
                high DECIMAL(10, 2),
                low DECIMAL(10, 2),
                volume INT,
                circuit_breaker VARCHAR(255),
                lower_cap DECIMAL(10, 2),
                higher_cap DECIMAL(10, 2),
                day_range VARCHAR(255),
                week_range_52 VARCHAR(255),
                week_lower_52 DECIMAL(10, 2),
                week_higher_52 DECIMAL(10, 2),
                sector VARCHAR(255),
                ldcp DECIMAL(10, 2),
                var DECIMAL(10, 2),
                haircut DECIMAL(10, 2),
                pe_ratio_ttm DECIMAL(10, 2),
                one_year_change DECIMAL(10, 2),
                ytd_change DECIMAL(10, 2),
                pe_ratio DECIMAL(10, 2),
                `2023` DECIMAL(10, 2),
                `2022` DECIMAL(10, 2),
                `2021` DECIMAL(10, 2),
                `2020` DECIMAL(10, 2)
            )
            """
            cursor.execute(create_table_query)
            conn.commit()

            # Insert the data into the database
            insert_query = """
            INSERT INTO stock_data
            (symbol, price, change_value, change_percentage, open_value, high, low, volume, circuit_breaker, lower_cap, higher_cap, day_range, week_range_52, week_lower_52, week_higher_52, sector, ldcp, var, haircut, pe_ratio_ttm, one_year_change, ytd_change, pe_ratio, `2023`, `2022`, `2021`, `2020`)
            VALUES (%(symbol)s, %(price)s, %(change_value)s, %(change_percentage)s, %(open_value)s, %(high)s, %(low)s, %(volume)s, %(circuit_breaker)s, %(lower_cap)s, %(higher_cap)s, %(day_range)s, %(week_range_52)s, %(week_lower_52)s, %(week_higher_52)s, %(sector)s, %(ldcp)s, %(var)s, %(haircut)s, %(pe_ratio_ttm)s, %(one_year_change)s, %(ytd_change)s, %(pe_ratio)s, %(2023)s, %(2022)s, %(2021)s, %(2020)s)
            """
            cursor.execute(insert_query, stock_data)
            conn.commit()

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")

        finally:
            cursor.close()
            conn.close()