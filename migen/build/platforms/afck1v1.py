# Founded by Creotech Instruments S.A.
# www.creotech.pl

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

_io = [

# Clock inputs
# =========================================================================

    ("clk20", 0, Pins("AF6"), IOStandard("LVCMOS15")),

    ("fpga_clk", 0,
        Subsignal("p", Pins("AG10")),
        Subsignal("n", Pins("AH10")),
        Misc("DIFF_TERM=FALSE"),
        IOStandard("DIFF_SSTL15")),

# FMC1 Clocks

    ("fmc1_clk0_m2c", 0,
        Subsignal("p", Pins("C25")),
        Subsignal("n", Pins("B25")),
        IOStandard("LVDS_25")),

    ("fmc1_clk1_m2c", 0,
        Subsignal("p", Pins("F20")),
        Subsignal("n", Pins("E20")),
        IOStandard("LVDS_25")),

    ("fmc1_clk2_bidir", 0,
        Subsignal("p", Pins("D27")),
        Subsignal("n", Pins("C27")),
        IOStandard("LVDS_25")),

    ("fmc1_clk3_bidir", 0,
        Subsignal("p", Pins("D17")),
        Subsignal("n", Pins("D18")),
        IOStandard("LVDS_25")),

# FMC2 Clocks

    ("fmc2_clk0_m2c", 0,
        Subsignal("p", Pins("U27")),
        Subsignal("n", Pins("U28")),
        IOStandard("LVDS_25")),

    ("fmc2_clk1_m2c", 0,
        Subsignal("p", Pins("AG29")),
        Subsignal("n", Pins("AH29")),
        IOStandard("LVDS_25")),

    ("fmc2_clk2_bidir", 0,
        Subsignal("p", Pins("T26")),
        Subsignal("n", Pins("T27")),
        IOStandard("LVDS_25")),

    ("fmc2_clk3_bidir", 0,
        Subsignal("p", Pins("AB27")),
        Subsignal("n", Pins("AC27")),
        IOStandard("LVDS_25")),

# MGT Clocks

    ("mgt115_clk0", 0,
        Subsignal("p", Pins("R8")),
        Subsignal("n", Pins("R7"))),

    ("mgt115_clk1", 0,
         Subsignal("p", Pins("U8")),
         Subsignal("n", Pins("U7"))),

    ("mgt116_clk0", 0,
        Subsignal("p", Pins("L8")),
        Subsignal("n", Pins("L7"))),

    ("mgt116_clk1", 0,
         Subsignal("p", Pins("N8")),
         Subsignal("n", Pins("N7"))),

    ("mgt117_clk0", 0,
        Subsignal("p", Pins("G8")),
        Subsignal("n", Pins("G7"))),

    ("mgt117_clk1", 0,
         Subsignal("p", Pins("J8")),
         Subsignal("n", Pins("J7"))),

    ("mgt118_clk0", 0,
        Subsignal("p", Pins("C8")),
        Subsignal("n", Pins("C7"))),

    ("mgt118_clk1", 0,
         Subsignal("p", Pins("E8")),
         Subsignal("n", Pins("E7"))),

# GTX Transcivers
# =========================================================================

# MGT115

    ("mgt115", 0,
        Subsignal("txp", Pins("Y2")),
        Subsignal("txn", Pins("Y1")),
        Subsignal("rxp", Pins("AA4")),
        Subsignal("rxn", Pins("AA3"))),

    ("mgt115", 1,
        Subsignal("txp", Pins("V2")),
        Subsignal("txn", Pins("V1")),
        Subsignal("rxp", Pins("Y6")),
        Subsignal("rxn", Pins("Y5"))),

    ("mgt115", 2,
        Subsignal("txp", Pins("U4")),
        Subsignal("txn", Pins("U3")),
        Subsignal("rxp", Pins("W4")),
        Subsignal("rxn", Pins("W3"))),

    ("mgt115", 3,
        Subsignal("txp", Pins("T2")),
        Subsignal("txn", Pins("T1")),
        Subsignal("rxp", Pins("V6")),
        Subsignal("rxn", Pins("V5"))),

# MGT 116

    ("mgt116", 0,
         Subsignal("txp", Pins("P2")),
         Subsignal("txn", Pins("P1")),
         Subsignal("rxp", Pins("T6")),
         Subsignal("rxn", Pins("T5"))),

    ("mgt116", 1,
         Subsignal("txp", Pins("N4")),
         Subsignal("txn", Pins("N3")),
         Subsignal("rxp", Pins("R4")),
         Subsignal("rxn", Pins("R3"))),

    ("mgt116", 2,
         Subsignal("txp", Pins("M2")),
         Subsignal("txn", Pins("M1")),
         Subsignal("rxp", Pins("P6")),
         Subsignal("rxn", Pins("P5"))),

    ("mgt116", 3,
         Subsignal("txp", Pins("L4")),
         Subsignal("txn", Pins("L3")),
         Subsignal("rxp", Pins("M6")),
         Subsignal("rxn", Pins("M5"))),

# MGT 117

    ("mgt117", 0,
         Subsignal("txp", Pins("K2")),
         Subsignal("txn", Pins("K1")),
         Subsignal("rxp", Pins("K6")),
         Subsignal("rxn", Pins("K5"))),

    ("mgt117", 1,
         Subsignal("txp", Pins("J4")),
         Subsignal("txn", Pins("J3")),
         Subsignal("rxp", Pins("H6")),
         Subsignal("rxn", Pins("H5"))),

    ("mgt117", 2,
         Subsignal("txp", Pins("H2")),
         Subsignal("txn", Pins("H1")),
         Subsignal("rxp", Pins("G4")),
         Subsignal("rxn", Pins("G3"))),

    ("mgt117", 3,
         Subsignal("txp", Pins("F2")),
         Subsignal("txn", Pins("F1")),
         Subsignal("rxp", Pins("F6")),
         Subsignal("rxn", Pins("F5"))),

# MGT 118

    ("mgt118", 0,
         Subsignal("txp", Pins("D2")),
         Subsignal("txn", Pins("D1")),
         Subsignal("rxp", Pins("E4")),
         Subsignal("rxn", Pins("E3"))),

    ("mgt118", 1,
         Subsignal("txp", Pins("C4")),
         Subsignal("txn", Pins("C3")),
         Subsignal("rxp", Pins("D6")),
         Subsignal("rxn", Pins("D5"))),

    ("mgt118", 2,
         Subsignal("txp", Pins("B2")),
         Subsignal("txn", Pins("B1")),
         Subsignal("rxp", Pins("B6")),
         Subsignal("rxn", Pins("B5"))),

    ("mgt118", 3,
         Subsignal("txp", Pins("A4")),
         Subsignal("txn", Pins("A3")),
         Subsignal("rxp", Pins("A8")),
         Subsignal("rxn", Pins("A7"))),

# RTM IO
# =========================================================================

    ("rtm_io", 0, Pins("P19"), IOStandard("LVCMOS25")),
    ("rtm_io", 1, Pins("M19"), IOStandard("LVCMOS25")),
    ("rtm_io", 2, Pins("L11"), IOStandard("LVCMOS25")),
    ("rtm_io", 3, Pins("F15"), IOStandard("LVCMOS25")),
    ("rtm_io", 4, Pins("E18"), IOStandard("LVCMOS25")),
    ("rtm_io", 5, Pins("C20"), IOStandard("LVCMOS25")),
    ("rtm_io", 6, Pins("H24"), IOStandard("LVCMOS25")),
    ("rtm_io", 7, Pins("AA25"), IOStandard("LVCMOS25")),
    ("rtm_io", 8, Pins("V19"), IOStandard("LVCMOS25")),
    ("rtm_io", 9, Pins("R24"), IOStandard("LVCMOS25")),
    ("rtm_io", 10, Pins("AE15"), IOStandard("LVCMOS18")),
    ("rtm_io", 11, Pins("AB7"), IOStandard("LVCMOS15")),
    ("rtm_io", 12, Pins("AC6"), IOStandard("LVCMOS15")),
    ("rtm_io", 13, Pins("AH4"), IOStandard("LVCMOS15")),

    ("rtm_lvds", 0,
        Subsignal("p", Pins("H20")),
        Subsignal("n", Pins("G20")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 1,
        Subsignal("p", Pins("H21")),
        Subsignal("n", Pins("H22")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 2,
        Subsignal("p", Pins("AH26")),
        Subsignal("n", Pins("AH27")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 3,
        Subsignal("p", Pins("AC29")),
        Subsignal("n", Pins("AC30")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 4,
        Subsignal("p", Pins("AK29")),
        Subsignal("n", Pins("AK30")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 5,
        Subsignal("p", Pins("E24")),
        Subsignal("n", Pins("D24")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 6,
        Subsignal("p", Pins("E23")),
        Subsignal("n", Pins("D23")),
        IOStandard("LVDS_25")),

    ("rtm_lvds", 7,
        Subsignal("p", Pins("G22")),
        Subsignal("n", Pins("F22")),
        IOStandard("LVDS_25")),

# AMC MLVDS
# =========================================================================

    ("amc_mlvds_io", 0, Pins("AA10"), IOStandard("LVCMOS15")),  # IO_RX_P17
    ("amc_mlvds_io", 1, Pins("AA12"), IOStandard("LVCMOS15")),  # IO_TX_P17
    ("amc_mlvds_io", 2, Pins("AC10"), IOStandard("LVCMOS15")),  # IO_RX_P18
    ("amc_mlvds_io", 3, Pins("AE8"), IOStandard("LVCMOS15")),   # IO_TX_P18
    ("amc_mlvds_io", 4, Pins("AB9"), IOStandard("LVCMOS15")),   # IO_RX_P19
    ("amc_mlvds_io", 5, Pins("AB8"), IOStandard("LVCMOS15")),   # IO_TX_P19
    ("amc_mlvds_io", 6, Pins("AA8"), IOStandard("LVCMOS15")),   # IO_RX_P20
    ("amc_mlvds_io", 7, Pins("Y10"), IOStandard("LVCMOS15")),   # IO_TX_P20

    ("amc_mlvds_dir", 0, Pins("Y11"), IOStandard("LVCMOS15")),  # IO_RX_P17
    ("amc_mlvds_dir", 1, Pins("AA11"), IOStandard("LVCMOS15")), # IO_TX_P17
    ("amc_mlvds_dir", 2, Pins("AD8"), IOStandard("LVCMOS15")),  # IO_RX_P18
    ("amc_mlvds_dir", 3, Pins("AA13"), IOStandard("LVCMOS15")), # IO_TX_P18
    ("amc_mlvds_dir", 4, Pins("AB12"), IOStandard("LVCMOS15")), # IO_RX_P19
    ("amc_mlvds_dir", 5, Pins("AC12"), IOStandard("LVCMOS15")), # IO_TX_P19
    ("amc_mlvds_dir", 6, Pins("AB10"), IOStandard("LVCMOS15")), # IO_RX_P20
    ("amc_mlvds_dir", 7, Pins("AC9"), IOStandard("LVCMOS15")),  # IO_TX_P20

# Carrier Peripherals
# =========================================================================

    ("serial", 0,
        Subsignal("rx", Pins("F16")),
        Subsignal("tx", Pins("G12")),
        IOStandard("LVCMOS25")),

    ("i2c", 0,
        Subsignal("scl", Pins("K19")),
        Subsignal("sda", Pins("G19")),
        IOStandard("LVCMOS25")),

    ("spiflash", 0,
        Subsignal("cs_n", Pins("U19")),
        Subsignal("dq", Pins("P24 R25 R20 R21")),
        IOStandard("LVCMOS25")
     ),

    ("spiflash2x", 0,
        Subsignal("cs_n", Pins("U19")),
        Subsignal("dq", Pins("P24 R25")),
        Subsignal("wp", Pins("R20")),
        Subsignal("hold", Pins("R21")),
        IOStandard("LVCMOS25")
    ),

    ("led", 0, Pins("G23"), IOStandard("LVCMOS25")),
    ("led", 1, Pins("G25"), IOStandard("LVCMOS25")),
    ("led", 2, Pins("F23"), IOStandard("LVCMOS25")),

    ("si570_en", 0, Pins("Y20"), IOStandard("LVCMOS25")),
    ("adn4604_nupdate", 0, Pins("AE16"), IOStandard("LVCMOS18")),

    ("vcxo_dac1_sync_n", 0, Pins("Y14"), IOStandard("LVCMOS18")),
    ("vcxo_dac2_sync_n", 0, Pins("AB14"), IOStandard("LVCMOS18")),
    ("vcxo_dac_din", 0, Pins("Y25"), IOStandard("LVCMOS25")),
    ("vcxo_dac_sclk", 0, Pins("AE26"), IOStandard("LVCMOS25")),

    ("ddram", 0,

            # FIXME: MiSOC RAM controller does not seem to cooperate with multiple memory devices

            Subsignal("a", Pins("AF10 AJ12 AK10 AJ11 AF12 AK11 AH14 AG13 AJ14 AH11 AG9 AH12 AG12 AK13 AJ13 AD11"),
                IOStandard("SSTL15")),
            Subsignal("ba", Pins("AK9 AH9 AE13"), IOStandard("SSTL15")),
            Subsignal("ras_n", Pins("AD9"), IOStandard("SSTL15")),
            Subsignal("cas_n", Pins("AC11"), IOStandard("SSTL15")),
            Subsignal("we_n", Pins("AJ9"), IOStandard("SSTL15")),
            Subsignal("cs_n", Pins("AE10"), IOStandard("SSTL15")),
            Subsignal("dm", Pins("AD3 AF3 AH2 AK6"), IOStandard("SSTL15")),
            # Subsignal("dm", Pins("AD3 AF3"), IOStandard("SSTL15")),
            # Subsignal("dq", Pins("AC4 AC2 AC7 AC1 AD4 AD6 AC5 AE6 AE1 AF2 AE4 AF5 AE3 AG5 AE5 AF1"),
            #                 IOStandard("SSTL15_T_DCI")),
            Subsignal("dq", Pins("AC4 AC2 AC7 AC1 AD4 AD6 AC5 AE6 AE1 AF2 AE4 AF5 AE3 AG5 AE5 AF1 "
                                 "AJ1 AK3 AH5 AJ3 AJ2 AJ4 AH6 AK1 AK5 AJ6 AF8 AJ8 AG7 AK8 AF7 AK4"),
                            IOStandard("SSTL15_T_DCI")),
            Subsignal("dqs_p", Pins("AD2 AG4 AG2 AH7"), IOStandard("DIFF_SSTL15")),
            # Subsignal("dqs_p", Pins("AD2 AG4"), IOStandard("DIFF_SSTL15")),
            Subsignal("dqs_n", Pins("AD1 AG3 AH1 AJ7"), IOStandard("DIFF_SSTL15")),
            # Subsignal("dqs_n", Pins("AD1 AG3"), IOStandard("DIFF_SSTL15")),
            Subsignal("clk_p", Pins("AE11"), IOStandard("DIFF_SSTL15")),
            Subsignal("clk_n", Pins("AF11"), IOStandard("DIFF_SSTL15")),
            Subsignal("cke", Pins("AD12"), IOStandard("SSTL15")),
            Subsignal("odt", Pins("AE9"), IOStandard("SSTL15")),
            Subsignal("reset_n", Pins("AK14"), IOStandard("LVCMOS15")),
            Misc("SLEW=FAST")
        ),

]

_connectors = [
    ("fmc1", {
        "HA00_N": "K29",
        "HA00_P": "K28",
        "HA01_N": "L27",
        "HA01_P": "L26",
        "HA02_N": "L28",
        "HA02_P": "M28",
        "HA03_N": "N30",
        "HA03_P": "N29",
        "HA04_N": "K30",
        "HA04_P": "L30",
        "HA05_N": "M30",
        "HA05_P": "M29",
        "HA06_N": "K21",
        "HA06_P": "L21",
        "HA07_N": "H29",
        "HA07_P": "J29",
        "HA08_N": "J28",
        "HA08_P": "J27",
        "HA09_N": "M27",
        "HA09_P": "N27",
        "HA10_N": "L23",
        "HA10_P": "L22",
        "HA11_N": "K24",
        "HA11_P": "K23",
        "HA12_N": "J26",
        "HA12_P": "K26",
        "HA13_N": "N26",
        "HA13_P": "N25",
        "HA14_N": "J24",
        "HA14_P": "J23",
        "HA15_N": "N24",
        "HA15_P": "P23",
        "HA16_N": "M25",
        "HA16_P": "M24",
        "HA17_N": "K25",
        "HA17_P": "L25",
        "HA18_N": "J22",
        "HA18_P": "J21",
        "HA19_N": "N22",
        "HA19_P": "N21",
        "HA20_N": "M23",
        "HA20_P": "M22",
        "HA21_N": "P22",
        "HA21_P": "P21",
        "HA22_N": "L20",
        "HA22_P": "M20",
        "HA23_N": "N20",
        "HA23_P": "N19",
        "HB00_N": "F13",
        "HB00_P": "G13",
        "HB01_N": "H16",
        "HB01_P": "J16",
        "HB02_N": "K15",
        "HB02_P": "L15",
        "HB03_N": "K16",
        "HB03_P": "L16",
        "HB04_N": "E15",
        "HB04_P": "E14",
        "HB05_N": "B15",
        "HB05_P": "C15",
        "HB06_N": "G14",
        "HB06_P": "H14",
        "HB07_N": "G15",
        "HB07_P": "H15",
        "HB08_N": "B12",
        "HB08_P": "C12",
        "HB09_N": "J14",
        "HB09_P": "K14",
        "HB10_N": "A15",
        "HB10_P": "B14",
        "HB11_N": "E13",
        "HB11_P": "F12",
        "HB12_N": "J12",
        "HB12_P": "J11",
        "HB13_N": "H12",
        "HB13_P": "H11",
        "HB14_N": "C14",
        "HB14_P": "D14",
        "HB15_N": "E11",
        "HB15_P": "F11",
        "HB16_N": "L13",
        "HB16_P": "L12",
        "HB17_N": "D13",
        "HB17_P": "D12",
        "HB18_N": "A13",
        "HB18_P": "B13",
        "HB19_N": "J13",
        "HB19_P": "K13",
        "HB20_N": "A12",
        "HB20_P": "A11",
        "HB21_N": "C11",
        "HB21_P": "D11",
        "LA00_N": "C26",
        "LA00_P": "D26",
        "LA01_N": "D28",
        "LA01_P": "E28",
        "LA02_N": "F27",
        "LA02_P": "G27",
        "LA03_N": "G30",
        "LA03_P": "H30",
        "LA04_N": "F30",
        "LA04_P": "G29",
        "LA05_N": "C30",
        "LA05_P": "D29",
        "LA06_N": "F28",
        "LA06_P": "G28",
        "LA07_N": "A30",
        "LA07_P": "B30",
        "LA08_N": "E30",
        "LA08_P": "E29",
        "LA09_N": "B24",
        "LA09_P": "C24",
        "LA10_N": "B29",
        "LA10_P": "C29",
        "LA11_N": "A26",
        "LA11_P": "A25",
        "LA12_N": "A28",
        "LA12_P": "B28",
        "LA13_N": "A23",
        "LA13_P": "B23",
        "LA14_N": "E25",
        "LA14_P": "F25",
        "LA15_N": "H27",
        "LA15_P": "H26",
        "LA16_N": "E26",
        "LA16_P": "F26",
        "LA17_N": "D19",
        "LA17_P": "E19",
        "LA18_N": "E21",
        "LA18_P": "F21",
        "LA19_N": "A22",
        "LA19_P": "B22",
        "LA20_N": "A21",
        "LA20_P": "A20",
        "LA21_N": "L18",
        "LA21_P": "L17",
        "LA22_N": "H17",
        "LA22_P": "J17",
        "LA23_N": "C22",
        "LA23_P": "D22",
        "LA24_N": "B19",
        "LA24_P": "C19",
        "LA25_N": "A18",
        "LA25_P": "B18",
        "LA26_N": "A17",
        "LA26_P": "A16",
        "LA27_N": "C16",
        "LA27_P": "D16",
        "LA28_N": "H19",
        "LA28_P": "J19",
        "LA29_N": "C21",
        "LA29_P": "D21",
        "LA30_N": "F18",
        "LA30_P": "G18",
        "LA31_N": "J18",
        "LA31_P": "K18",
        "LA32_N": "F17",
        "LA32_P": "G17",
        "LA33_N": "B17",
        "LA33_P": "C17",
    }),
    ("fmc2", {
        "HA00_N": "AH24",
        "HA00_P": "AG24",
        "HA01_N": "AG23",
        "HA01_P": "AF22",
        "HA02_N": "AH20",
        "HA02_P": "AG20",
        "HA03_N": "AK25",
        "HA03_P": "AJ24",
        "HA04_N": "AF21",
        "HA04_P": "AF20",
        "HA05_N": "AH25",
        "HA05_P": "AG25",
        "HA06_N": "AK24",
        "HA06_P": "AK23",
        "HA07_N": "AK21",
        "HA07_P": "AK20",
        "HA08_N": "AJ21",
        "HA08_P": "AH21",
        "HA09_N": "AJ23",
        "HA09_P": "AJ22",
        "HA10_N": "AE21",
        "HA10_P": "AD21",
        "HA11_N": "AH22",
        "HA11_P": "AG22",
        "HA12_N": "AF23",
        "HA12_P": "AE23",
        "HA13_N": "AC21",
        "HA13_P": "AC20",
        "HA14_N": "AB23",
        "HA14_P": "AB22",
        "HA15_N": "AD22",
        "HA15_P": "AC22",
        "HA16_N": "AF25",
        "HA16_P": "AE25",
        "HA17_N": "AE24",
        "HA17_P": "AD23",
        "HA18_N": "AB20",
        "HA18_P": "AA20",
        "HA19_N": "AC25",
        "HA19_P": "AB24",
        "HA20_N": "AD24",
        "HA20_P": "AC24",
        "HA21_N": "AA21",
        "HA21_P": "Y21",
        "HA22_N": "AA23",
        "HA22_P": "AA22",
        "HA23_N": "Y24",
        "HA23_P": "Y23",
        "HB00_N": "AG18",
        "HB00_P": "AF18",
        "HB01_N": "AJ16",
        "HB01_P": "AH16",
        "HB02_N": "AH15",
        "HB02_P": "AG15",
        "HB03_N": "AK15",
        "HB03_P": "AK16",
        "HB04_N": "AK19",
        "HB04_P": "AJ19",
        "HB05_N": "AK18",
        "HB05_P": "AJ18",
        "HB06_N": "AG17",
        "HB06_P": "AF17",
        "HB07_N": "AJ17",
        "HB07_P": "AH17",
        "HB08_N": "AG14",
        "HB08_P": "AF15",
        "HB09_N": "AH19",
        "HB09_P": "AG19",
        "HB10_N": "AC17",
        "HB10_P": "AB17",
        "HB11_N": "AC19",
        "HB11_P": "AB19",
        "HB12_N": "AD16",
        "HB12_P": "AD17",
        "HB13_N": "AE19",
        "HB13_P": "AD19",
        "HB14_N": "AB15",
        "HB14_P": "AA15",
        "HB15_N": "Y15",
        "HB15_P": "Y16",
        "HB16_N": "AD14",
        "HB16_P": "AC14",
        "HB17_N": "AE18",
        "HB17_P": "AD18",
        "HB18_N": "AA16",
        "HB18_P": "AA17",
        "HB19_N": "AC15",
        "HB19_P": "AC16",
        "HB20_N": "Y18",
        "HB20_P": "Y19",
        "HB21_N": "AB18",
        "HB21_P": "AA18",
        "LA00_N": "AF28",
        "LA00_P": "AE28",
        "LA01_N": "AD28",
        "LA01_P": "AD27",
        "LA02_N": "AK26",
        "LA02_P": "AJ26",
        "LA03_N": "AA26",
        "LA03_P": "Y26",
        "LA04_N": "AB30",
        "LA04_P": "AB29",
        "LA05_N": "AJ29",
        "LA05_P": "AJ28",
        "LA06_N": "AK28",
        "LA06_P": "AJ27",
        "LA07_N": "AB28",
        "LA07_P": "AA27",
        "LA08_N": "AG28",
        "LA08_P": "AG27",
        "LA09_N": "AF27",
        "LA09_P": "AF26",
        "LA10_N": "AA30",
        "LA10_P": "Y30",
        "LA11_N": "W28",
        "LA11_P": "W27",
        "LA12_N": "AH30",
        "LA12_P": "AG30",
        "LA13_N": "AA28",
        "LA13_P": "Y28",
        "LA14_N": "Y29",
        "LA14_P": "W29",
        "LA15_N": "AF30",
        "LA15_P": "AE30",
        "LA16_N": "AE29",
        "LA16_P": "AD29",
        "LA17_N": "U25",
        "LA17_P": "T25",
        "LA18_N": "T28",
        "LA18_P": "R28",
        "LA19_N": "W26",
        "LA19_P": "V25",
        "LA20_N": "V27",
        "LA20_P": "V26",
        "LA21_N": "V30",
        "LA21_P": "V29",
        "LA22_N": "V22",
        "LA22_P": "V21",
        "LA23_N": "W22",
        "LA23_P": "W21",
        "LA24_N": "U30",
        "LA24_P": "U29",
        "LA25_N": "W24",
        "LA25_P": "W23",
        "LA26_N": "V24",
        "LA26_P": "U24",
        "LA27_N": "U23",
        "LA27_P": "U22",
        "LA28_N": "T23",
        "LA28_P": "T22",
        "LA29_N": "T21",
        "LA29_P": "T20",
        "LA30_N": "R26",
        "LA30_P": "P26",
        "LA31_N": "T30",
        "LA31_P": "R30",
        "LA32_N": "P28",
        "LA32_P": "P27",
        "LA33_N": "R29",
        "LA33_P": "P29",
    })
]


class Platform(XilinxPlatform):
    default_clk_name = "clk20"
    default_clk_period = 50.0

    def __init__(self):

        XilinxPlatform.__init__(self, "xc7k325tffg900-3", _io, _connectors, toolchain="vivado")
        self.toolchain.bitstream_commands.extend([
            "set_property BITSTREAM.CONFIG.OVERTEMPPOWERDOWN Enable [current_design]",
            "set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]",
            "set_property CONFIG_MODE SPIx1 [current_design]",
            "set_property CFGBVS VCCO [current_design]",
            "set_property CONFIG_VOLTAGE 2.5 [current_design]",
            ])
