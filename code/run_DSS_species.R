library(DSS)
args = commandArgs(trailingOnly=TRUE)

###############################################################

#Cov <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_Cov.txt",header=T,sep="\t",check.names=FALSE))
#M <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_M.txt",header=T,sep="\t",check.names=FALSE))
#Loci <- read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region.info.txt",header=T,sep="\t",check.names=FALSE)
#bs.combine.filtered <- BSseq(chr = Loci$chr, pos = Loci$start , M = M, Cov = Cov, sampleNames = colnames(M))

bs.combine.filtered <- readRDS(args[1])
###do not change#############################################################
macaq.ind <- sampleNames(bs.combine.filtered)[grep("YN",sampleNames(bs.combine.filtered))]
human.ind <-sampleNames(bs.combine.filtered)[grep("Control",sampleNames(bs.combine.filtered))]
chimp.ind <- sampleNames(bs.combine.filtered)[!(sampleNames(bs.combine.filtered) %in% c(human.ind,macaq.ind))]
covariates_R <- read.table("../../bsseq/matrix/covariates_all.txt",header=T)
row.names(covariates_R) <- covariates_R$GT_ID

####################################################################

bs.species.CH <- bs.combine.filtered[,c(chimp.ind,human.ind)]
bs.species.CM <- bs.combine.filtered[,c(chimp.ind,macaq.ind)]
bs.species.HM <- bs.combine.filtered[,c(human.ind,macaq.ind)]

###########

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.combine.filtered)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.combine.filtered)$CellType <- covariates_R_order$CellType
pData(bs.combine.filtered)$Species <- covariates_R_order$Species
pData(bs.combine.filtered)$Sex <- covariates_R_order$Sex
pData(bs.combine.filtered)$Age_Class <- covariates_R_order$Age_Class
pData(bs.combine.filtered)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.combine.filtered)<- droplevels(pData(bs.combine.filtered))
pData(bs.combine.filtered)$Species <- factor(pData(bs.combine.filtered)$Species, levels = c("Human", "Chimp", "Macaque"))

############

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.species.CH)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.species.CH)$CellType <- covariates_R_order$CellType
pData(bs.species.CH)$Species <- covariates_R_order$Species
pData(bs.species.CH)$Sex <- covariates_R_order$Sex
pData(bs.species.CH)$Age_Class <- covariates_R_order$Age_Class
pData(bs.species.CH)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.species.CH)<- droplevels(pData(bs.species.CH))

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.species.CM)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.species.CM)$CellType <- covariates_R_order$CellType
pData(bs.species.CM)$Species <- covariates_R_order$Species
pData(bs.species.CM)$Sex <- covariates_R_order$Sex
pData(bs.species.CM)$Age_Class <- covariates_R_order$Age_Class
pData(bs.species.CM)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.species.CM)<- droplevels(pData(bs.species.CM))

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.species.HM)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.species.HM)$CellType <- covariates_R_order$CellType
pData(bs.species.HM)$Species <- covariates_R_order$Species
pData(bs.species.HM)$Sex <- covariates_R_order$Sex
pData(bs.species.HM)$Age_Class <- covariates_R_order$Age_Class
pData(bs.species.HM)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.species.HM)<- droplevels(pData(bs.species.HM))

##################

#model.matrix(~Species+CellType+Sex+Age_Class+Conversion_rates+Species:CellType,pData(bs.PR.olig))
#SpeciesHuman SpeciesMacaque CellTypeOlig SpeciesHuman:CellTypeOlig


###############

DMLfit = DMLfit.multiFactor(bs.combine.filtered,pData(bs.combine.filtered), ~Species+Sex+Age_Class+Conversion_rates)
DMLtest = DMLtest.multiFactor(DMLfit, term="Species")
write.table(DMLtest,file=paste0(args[2],"_Species.txt"),sep="\t",row.names=F,quote=F)

DMLfit = DMLfit.multiFactor(bs.species.CH,pData(bs.species.CH), ~Species+Sex+Age_Class+Conversion_rates)
DMLtest = DMLtest.multiFactor(DMLfit, coef="SpeciesHuman")
write.table(DMLtest,file=paste0(args[2],"_Species_HvsC.txt"),sep="\t",row.names=F,quote=F)
pval_max <- DMLtest[DMLtest$pvals<0.005,][which.max(DMLtest[DMLtest$pvals<0.005,]$pvals),]
DMRtest <- callDMR(DMLtest, p.threshold=0.005,minCG=4)
DMRtest_filtered <- DMRtest[(abs(DMRtest$areaStat) / DMRtest$nCG) > abs(pval_max$stat),]
write.table(DMRtest,file=paste0(args[2],"_Species_HvsC.DMR.fdrs.txt"),sep="\t",row.names=F,quote=F)
write.table(DMRtest_filtered,file=paste0(args[2],"_Species_HvsC.DMR.fdrs.filtered.txt"),sep="\t",row.names=F,quote=F)

DMLfit = DMLfit.multiFactor(bs.species.CM,pData(bs.species.CM), ~Species+Sex+Age_Class+Conversion_rates)
DMLtest = DMLtest.multiFactor(DMLfit, coef="SpeciesMacaque")
write.table(DMLtest,file=paste0(args[2],"_Species_MvsC.txt"),sep="\t",row.names=F,quote=F)
pval_max <- DMLtest[DMLtest$pvals<0.005,][which.max(DMLtest[DMLtest$pvals<0.005,]$pvals),]
DMRtest <- callDMR(DMLtest, p.threshold=0.005,minCG=4)
DMRtest_filtered <- DMRtest[(abs(DMRtest$areaStat) / DMRtest$nCG) > abs(pval_max$stat),]
write.table(DMRtest,file=paste0(args[2],"_Species_MvsC.DMR.fdrs.txt"),sep="\t",row.names=F,quote=F)
write.table(DMRtest_filtered,file=paste0(args[2],"_Species_MvsC.DMR.fdrs.filtered.txt"),sep="\t",row.names=F,quote=F)

DMLfit = DMLfit.multiFactor(bs.species.HM,pData(bs.species.HM), ~Species+Sex+Age_Class+Conversion_rates)
DMLtest = DMLtest.multiFactor(DMLfit, coef="SpeciesMacaque")
write.table(DMLtest,file=paste0(args[2],"_Species_MvsH.txt"),sep="\t",row.names=F,quote=F)
pval_max <- DMLtest[DMLtest$pvals<0.005,][which.max(DMLtest[DMLtest$pvals<0.005,]$pvals),]
DMRtest <- callDMR(DMLtest, p.threshold=0.005,minCG=4)
DMRtest_filtered <- DMRtest[(abs(DMRtest$areaStat) / DMRtest$nCG) > abs(pval_max$stat),]
write.table(DMRtest,file=paste0(args[2],"_Species_MvsH.DMR.fdrs.txt"),sep="\t",row.names=F,quote=F)
write.table(DMRtest_filtered,file=paste0(args[2],"_Species_MvsH.DMR.fdrs.filtered.txt"),sep="\t",row.names=F,quote=F)

##############

