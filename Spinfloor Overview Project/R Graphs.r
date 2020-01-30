# Plot scatter plot for Power BI

library(ggplot2)
library(scales)
library(dplyr)

dataset$production_time <- as.POSIXct(dataset$production_time)

ggplot(dataset, aes(x=production_time, y=test_result_value),fill="red") + 
    geom_point() +
    scale_x_datetime(date_breaks = "7 day", labels = date_format("%d %b")) +
    theme(axis.text.x = element_text(angle = 25, vjust = 1.0, hjust = 1.0)) +
    xlab("Test Result Value") + 
    ylab("Production Time") +
    geom_hline(data=dataset,aes(yintercept=as.numeric(aim), col = "red")) +
    geom_hline(data=dataset,aes(yintercept=as.numeric(limit_high), col = "blue")) +
    geom_hline(data=dataset,aes(yintercept=as.numeric(limit_low), col = "green")) +
    scale_color_identity(labels=c("Limit High","Limit Low","Aim"), guide="legend")

# Plot Histogram

library(ggplot2)
library(gtable)
library(grid)

p1 <- ggplot(dataset, aes(x=test_result_value)) + 
    geom_histogram(aes(y=..density..), fill="steelblue3",alpha=0.6) +
    geom_density(aes(y=..density..), col="black") +
    facet_wrap(~property,scales="free") +
    xlab("Test Result Value") + 
    ylab("Density") +
    geom_vline(data=dataset,aes(xintercept=as.numeric(aim), col = "red")) +
    geom_vline(data=dataset,aes(xintercept=as.numeric(limit_high), col = "blue")) +
    geom_vline(data=dataset,aes(xintercept=as.numeric(limit_low), col = "green")) +
    scale_color_identity(labels=c("Limit High","Limit Low","Aim"), guide="legend")

p1

# Plot Boxplot

library(ggplot2)
library(gtable)
library(grid)

p1 <- ggplot(dataset, aes(x=as.factor(cell), y=test_result_value, fill=property)) + 
    geom_boxplot() +
    facet_wrap(~property, dir="v",scales="free") +
    xlab("Cell") + 
    ylab("Test Result Value") + 
    geom_hline(data=dataset,aes(yintercept=as.numeric(aim), col = "red")) +
    geom_hline(data=dataset,aes(yintercept=as.numeric(limit_high), col = "blue")) +
    geom_hline(data=dataset,aes(yintercept=as.numeric(limit_low), col = "green")) +
    scale_color_identity(labels=c("Limit High","Limit Low","Aim"), guide="legend")

p1