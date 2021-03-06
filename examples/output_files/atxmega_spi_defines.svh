//----------------------------------------------------------------------------------------------------------------------------
// Autogenerated file -- DO NOT EDIT
//
// This file was autogenerated by PeakRDL-svh
// Date (mm-dd-yyyy) : 07-08-2020  
// Time (hh:mm:ss)   : 17:00:19
//
// This header contains:
// * Register and register field specifiers
// * Position values for fields
// * Mask values for fields
//----------------------------------------------------------------------------------------------------------------------------

`ifndef _ATXMEGA_SPI_DEFINES_INCLUDED_
`define _ATXMEGA_SPI_DEFINES_INCLUDED_

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
// Register:    Control Register
// Description: 
// Access:      RW
//
// Fields:
//     NAME                           WID   POS TYPE RESET       DESCRIPTION
//
//     CLK2X                          1       7 RW   0x0         When this bit is set, the SPI speed (SCK frequency) will be
//                                                               doubled in master mode
//
//     ENABLE                         1       6 RW   0x0         Setting this bit enables the SPI module. This bit must be
//                                                               set to enable any SPI operations
//
//     DORD                           1       5 RW   0x0         DORD decides the data order when a byte is shifted out from
//                                                               the DATA register. When DORD is written to one, the least-
//                                                               significant bit (lsb) of the data byte is transmitted first,
//                                                               and when DORD is written to zero, the most-significant bit
//                                                               (msb) of the data byte is transmitted first
//
//     MASTER                         1       4 RW   0x0         Selects master mode when written to one, and slave mode when
//                                                               written to zero. If SS is configured as an input and driven
//                                                               low while master mode is set, master mode will be cleared
//
//     MODE                           2   03:02 RW   0x0         These bits select the transfer mode
//
//     PRESCALER                      2   01:00 RW   0x0         Controls the SPI clock rate when configured in master mode
//
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

`define POS_CTRL_CLK2X                                                             7
`define POS_CTRL_ENABLE                                                            6
`define POS_CTRL_DORD                                                              5
`define POS_CTRL_MASTER                                                            4
`define POS_CTRL_MODE                                                              2
`define POS_CTRL_PRESCALER                                                         0

`define MASK_CTRL_CLK2X                                                   (1'h1<<`POS_CTRL_CLK2X)
`define MASK_CTRL_ENABLE                                                  (1'h1<<`POS_CTRL_ENABLE)
`define MASK_CTRL_DORD                                                    (1'h1<<`POS_CTRL_DORD)
`define MASK_CTRL_MASTER                                                  (1'h1<<`POS_CTRL_MASTER)
`define MASK_CTRL_MODE                                                    (2'h3<<`POS_CTRL_MODE)
`define MASK_CTRL_PRESCALER                                               (2'h3<<`POS_CTRL_PRESCALER)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
// Register:    Interrupt Control
// Description: 
// Access:      RW
//
// Fields:
//     NAME                           WID   POS TYPE RESET       DESCRIPTION
//
//     INTLVL                         2   01:00 RW   0x0         These bits enable the SPI interrupt and select the interrupt
//                                                               level
//
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

`define POS_INTCTRL_INTLVL                                                         0

`define MASK_INTCTRL_INTLVL                                               (2'h3<<`POS_INTCTRL_INTLVL)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
// Register:    STATUS
// Description: 
// Access:      RW
//
// Fields:
//     NAME                           WID   POS TYPE RESET       DESCRIPTION
//
//     IF                             1       7 RO   0x0         
//
//     WRCOL                          1       6 RO   0x0         
//
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

`define POS_STATUS_IF                                                              7
`define POS_STATUS_WRCOL                                                           6

`define MASK_STATUS_IF                                                    (1'h1<<`POS_STATUS_IF)
`define MASK_STATUS_WRCOL                                                 (1'h1<<`POS_STATUS_WRCOL)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
// Register:    DATA
// Description: The DATA register is used for sending and receiving data. Writing to the register initiates the data
//              transmission, and the byte written to the register will be shifted out on the SPI output line. Reading
//              the register causes the shift register receive buffer to be read, returning the last byte successfully
//              received
// Access:      RW
//
// Fields:
//     NAME                           WID   POS TYPE RESET       DESCRIPTION
//
//     RDATA                          8   07:00 RO   0x0         
//
//     WDATA                          8   07:00 WO   0x0         
//
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

`define POS_DATA_RDATA                                                             0
`define POS_DATA_WDATA                                                             0

`define MASK_DATA_RDATA                                                   (8'hff<<`POS_DATA_RDATA)
`define MASK_DATA_WDATA                                                   (8'hff<<`POS_DATA_WDATA)



`endif

