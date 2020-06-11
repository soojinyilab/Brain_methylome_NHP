library(bsseq)
args = commandArgs(trailingOnly=TRUE)

bs.filtered<- readRDS(args[1])

df.test <- read.table(file=args[2],header=T,sep="\t")
sub.grange<-makeGRangesFromDataFrame(df.test)
sub.meth.region <- getMeth(bs.filtered,regions=sub.grange,type="raw",what="perRegion")
write.csv(format(sub.meth.region,digits=3), file=args[3],row.names=F,quote=F)

