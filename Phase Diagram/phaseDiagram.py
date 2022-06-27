import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib import style
import numpy as np

#Styling plot

def phase(meltingPointA,meltingPointB,eutecticComposition,eutecticTemperature,solidusAEnd,solidusBEnd,solvusAEnd,solvusBEnd,testComposition,testTemperature):
    fig, ax = plt.subplots()
    #Setting figure width and height
    fig.set_figwidth(9)
    fig.set_figheight(7)

    xlim = 100
    ylim = max(meltingPointA,meltingPointB)+100
    plt.xlim([0,xlim])
    plt.ylim([0,ylim])

    #Adjust margins
    plt.subplots_adjust(left=0.067, right=0.97, top=0.95, bottom=0.07)
    majorTicksX = np.linspace(0,xlim,int(xlim/10)+1,endpoint=True)
    majorTicksY = np.linspace(0,ylim,int(ylim/100)+1,endpoint=True)
    minorTicksX= np.linspace(0,xlim,int(xlim/1)+1,endpoint=True)
    minorTicksY= np.linspace(0,ylim,int(ylim/10)+1,endpoint=True)


    ax.set_xticks(majorTicksX)
    ax.set_yticks(majorTicksY)
    ax.set_xticks(minorTicksX,minor=True)
    ax.set_yticks(minorTicksY,minor=True)
    ax.set_title("Phase Diagram")

    ax.grid(which="major",alpha=0.6)
    ax.grid(which="minor",alpha=0.3)

    # Percent formatter
    ax.xaxis.set_major_formatter(ticker.PercentFormatter())
   

    #Solidus(A) Line P(0,melt-temp) Q(solidus-end,eutectic-temp)
    plt.plot([0,solidusAEnd], [meltingPointA,eutecticTemperature], label = "Solidus(A) line", linestyle="-" ,c='k')
    plt.annotate("P", (0,meltingPointA))
    plt.annotate("Q", (solidusAEnd, eutecticTemperature))

    #Solvus(A) Line Q(solidus-end,eutectic-temp) R(solvus-end,0)
    plt.plot([solidusAEnd,solvusAEnd], [eutecticTemperature,0], label = "Solvus(A) line", linestyle="-" ,c='k')
    plt.annotate("R", (solvusAEnd,0))

    #Liquidus(A)  P(0,melt-temp) S(eutectic-composition,eutectic-temp)
    plt.plot([0,eutecticComposition], [meltingPointA,eutecticTemperature], label = "Liquidus(A) line", linestyle="-" ,c='k')
    plt.annotate("S", (eutecticComposition,eutecticTemperature))

    #Solidus(B) Line T(0,melt-temp) W(solidus-end,eutectic-temp)
    plt.plot([100,solidusBEnd], [meltingPointB,eutecticTemperature], label = "Solidus(B) line", linestyle="-" ,c='k')
    plt.annotate("T", (100,meltingPointB))
    plt.annotate("W", (solidusBEnd,eutecticTemperature))

    #Solvus(B) Line W(solidus-end,eutectic-temp) U(solvus-end,0)
    plt.plot([solidusBEnd,solvusBEnd], [eutecticTemperature,0], label = "Solvus(B) line", linestyle="-" ,c='k')
    plt.annotate("U", (solvusBEnd,0))

    #Liquidus(B)  P(0,melt-temp) S(eutectic-composition,eutectic-temp)
    plt.plot([100,eutecticComposition], [meltingPointB,eutecticTemperature], label = "Liquidus(B) line", linestyle="-" ,c='k')
    
    #Eutectic composition S(eutectic-composition,eutectic-temp) S'(eutectic-composition,0)
    plt.plot([eutecticComposition,eutecticComposition],[eutecticTemperature,0],  label = "Eutectic composition", linestyle="--" ,c='k')
    plt.annotate("S'", (eutecticComposition,0))

    #Eutectic Temperature Line Q(solidus(A)-end,eutectic-temp) W(solidus-end,eutectic-temp)
    plt.plot([solidusAEnd,solidusBEnd],[eutecticTemperature,eutecticTemperature],  label = "Eutectic temperature", linestyle="-." ,c='k')
   
    #Test composition line(MN)
    plt.plot([testComposition,testComposition],[testTemperature,0], linestyle=":" ,c='k')
    plt.annotate("N", (testComposition,0))
    plt.annotate("M", (testComposition,testTemperature))
   
    #Test temperature line(KJ)
    plt.plot([0,testComposition],[testTemperature,testTemperature], linestyle=":" ,c='k')
    plt.annotate("O", (testTemperature,0))
    #Test point
    plt.scatter([testComposition],[testTemperature],label='Test Composition' ,c='k')
   
    #Eutectic Temperature Line Q(solidus(A)-end,eutectic-temp) W(solidus-end,eutectic-temp)
    plt.plot([solidusAEnd,solidusBEnd],[eutecticTemperature,eutecticTemperature],  label = "Eutectic temperature", linestyle="--" ,c='k')
    plt.xlabel('Composition')
    plt.ylabel('Temperature(˚C)')  
    plt.legend(bbox_to_anchor=(0.7, 0.7))
    plt.show()
phase(900,800,60,700,20,90,10,95,40,775)