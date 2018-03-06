<Qucs Schematic 0.0.20>
<Properties>
  <View=10,87,1196,690,1.29975,0,0>
  <Grid=10,10,1>
  <DataSet=test4.dat>
  <DataDisplay=test4.dpl>
  <OpenDisplay=1>
  <Script=test4.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <GND * 1 270 560 0 0 0 0>
  <Vdc V3 1 270 400 18 -26 0 1 "5 V" 1>
  <GND * 1 380 550 0 0 0 0>
  <R R4 1 430 370 -26 -49 0 2 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <R R5 1 620 430 15 -26 0 1 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <GND * 1 620 490 0 0 0 0>
  <SpLib PMOS 1 550 340 -26 -74 0 2 "/home/leviathan/libresiliconprocess/simulation/pmos.lib" 0 "LV1UPMOS" 0 "auto" 0 "" 0>
  <GND * 1 590 550 0 0 0 0>
  <IProbe Pr1 1 410 170 -26 16 0 0>
  <Vrect V2 1 380 440 18 -26 0 1 "5 V" 1 "1 us" 1 "2 us" 1 "100 ns" 0 "100 ns" 0 "0 ns" 0>
  <SpLib NMOS 1 550 460 -26 51 1 2 "/home/leviathan/libresiliconprocess/simulation/nmos.lib" 0 "LV1UNMOS" 0 "auto" 0 "" 0>
  <.TR TR1 1 60 180 0 78 0 0 "lin" 1 "0" 1 "10 us" 1 "200" 0 "Trapezoidal" 0 "2" 0 "1 ns" 0 "1e-16" 0 "150" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "26.85" 0 "1e-3" 0 "1e-6" 0 "1" 0 "CroutLU" 0 "no" 0 "yes" 0 "0" 0>
</Components>
<Wires>
  <270 430 270 560 "" 0 0 0 "">
  <380 470 380 550 "" 0 0 0 "">
  <380 370 380 410 "" 0 0 0 "">
  <380 370 400 370 "" 0 0 0 "">
  <620 460 620 490 "" 0 0 0 "">
  <580 310 610 310 "" 0 0 0 "">
  <460 370 490 370 "" 0 0 0 "">
  <620 370 620 380 "" 0 0 0 "">
  <580 370 620 370 "output" 630 340 14 "">
  <490 430 520 430 "" 0 0 0 "">
  <490 370 520 370 "input" 469 390 30 "">
  <490 370 490 430 "" 0 0 0 "">
  <580 430 590 430 "" 0 0 0 "">
  <590 380 590 430 "" 0 0 0 "">
  <620 380 620 400 "" 0 0 0 "">
  <590 380 620 380 "" 0 0 0 "">
  <580 490 590 490 "" 0 0 0 "">
  <590 490 590 550 "" 0 0 0 "">
  <440 170 610 170 "" 0 0 0 "">
  <270 170 270 370 "" 0 0 0 "">
  <270 170 380 170 "" 0 0 0 "">
  <610 170 610 310 "" 0 0 0 "">
</Wires>
<Diagrams>
  <Rect 810 330 240 160 3 #c0c0c0 1 00 1 0 2e-05 0.0001 1 -4.26114 20 47.902 1 -1 1 1 315 0 225 "" "" "">
	<"ngspice/tran.v(output)" #ff0000 0 3 0 0 0>
	<"ngspice/tran.i(pr1)" #ff0000 0 3 0 0 0>
  </Rect>
  <Tab 760 656 386 206 3 #c0c0c0 1 00 1 0 1 1 1 0 1 1 1 0 1 2119 315 0 225 "" "" "">
	<"ngspice/tran.v(input)" #0000ff 0 3 1 0 0>
	<"ngspice/tran.v(output)" #0000ff 0 3 1 0 0>
  </Tab>
</Diagrams>
<Paintings>
</Paintings>
