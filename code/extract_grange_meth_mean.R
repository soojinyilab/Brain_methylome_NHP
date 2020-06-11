library(bsseq)
args = commandArgs(trailingOnly=TRUE)

bs.filtered<- readRDS(args[1])

df.test <- read.table(file=args[2],header=T,sep="\t")
sub.grange<-makeGRangesFromDataFrame(df.test)
sub.meth.region <- getMeth(bs.filtered,regions=sub.grange,type="raw",what="perRegion")
#write.csv(format(sub.meth.region,digits=3), file=args[3],row.names=F,quote=F)
Human_mean <- rowMeans(sub.meth.region[,1:10], na.rm=TRUE)
Chimp_mean <- rowMeans(sub.meth.region[,11:20], na.rm=TRUE)
Macaq_mean <- rowMeans(sub.meth.region[,21:30], na.rm=TRUE)
mean.meth.region <- data.frame(Human_mean=Human_mean,Chimp_mean=Chimp_mean,Macaq_mean=Macaq_mean)
write.csv(format(mean.meth.region,digits=3), file=args[3],row.names=F,quote=F)
