library(DSS)
args = commandArgs(trailingOnly=TRUE)

#HumanChimpMacaq_celltype_region_Cov.txt      HumanChimpMacaq_interaction_region_Cov.txt   HumanChimpMacaq_species_region_Cov.txt       tmp/
#HumanChimpMacaq_celltype_region.info.txt     HumanChimpMacaq_interaction_region.info.txt  HumanChimpMacaq_species_region.info.txt      
#HumanChimpMacaq_celltype_region_M.txt        HumanChimpMacaq_interaction_region_M.txt     HumanChimpMacaq_species_region_M.txt         

###############################################################

#Cov <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_celltype_region_Cov.txt",header=T,sep="\t",check.names=FALSE))
#M <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_celltype_region_M.txt",header=T,sep="\t",check.names=FALSE))
#Loci <- read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_celltype_region.info.txt",header=T,sep="\t",check.names=FALSE)
#bs.combine.filtered <- BSseq(chr = Loci$chr, pos = Loci$start , M = M, Cov = Cov, sampleNames = colnames(M))

#bs.combine.filtered <- readRDS("../5_DSS_input_ortho_cytosine/combined/rds/HCM_combine_CG.rds")
finput <- args[1]
bs.combine.filtered <- readRDS(finput)

###do not change#############################################################
macaq.ind <- sampleNames(bs.combine.filtered)[grep("YN",sampleNames(bs.combine.filtered))]
human.ind <-sampleNames(bs.combine.filtered)[grep("Control",sampleNames(bs.combine.filtered))]
chimp.ind <- sampleNames(bs.combine.filtered)[!(sampleNames(bs.combine.filtered) %in% c(human.ind,macaq.ind))]
covariates_R <- read.table("../../bsseq/matrix/covariates_all.txt",header=T)
row.names(covariates_R) <- covariates_R$GT_ID

####################################################################

bs.celltype.human <- bs.combine.filtered[,c(human.ind)]
bs.celltype.chimp <- bs.combine.filtered[,c(chimp.ind)]
bs.celltype.macaq <- bs.combine.filtered[,c(macaq.ind)]

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

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.celltype.human)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.celltype.human)$CellType <- covariates_R_order$CellType
pData(bs.celltype.human)$Species <- covariates_R_order$Species
pData(bs.celltype.human)$Sex <- covariates_R_order$Sex
pData(bs.celltype.human)$Age_Class <- covariates_R_order$Age_Class
pData(bs.celltype.human)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.celltype.human)<- droplevels(pData(bs.celltype.human))

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.celltype.chimp)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.celltype.chimp)$CellType <- covariates_R_order$CellType
pData(bs.celltype.chimp)$Species <- covariates_R_order$Species
pData(bs.celltype.chimp)$Sex <- covariates_R_order$Sex
pData(bs.celltype.chimp)$Age_Class <- covariates_R_order$Age_Class
pData(bs.celltype.chimp)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.celltype.chimp)<- droplevels(pData(bs.celltype.chimp))

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.celltype.macaq)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.celltype.macaq)$CellType <- covariates_R_order$CellType
pData(bs.celltype.macaq)$Species <- covariates_R_order$Species
pData(bs.celltype.macaq)$Sex <- covariates_R_order$Sex
pData(bs.celltype.macaq)$Age_Class <- covariates_R_order$Age_Class
pData(bs.celltype.macaq)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.celltype.macaq)<- droplevels(pData(bs.celltype.macaq))
############

##################

#bs.celltype.human <- bs.combine.filtered[,c(human.ind)]
#bs.celltype.chimp <- bs.combine.filtered[,c(chimp.ind)]
#bs.celltype.macaq <- bs.combine.filtered[,c(macaq.ind)]

#bs.species.CH <- bs.combine.filtered[,c(chimp.ind,human.ind)]
#bs.species.CM <- bs.combine.filtered[,c(chimp.ind,macaq.ind)]
#bs.species.HM <- bs.combine.filtered[,c(human.ind.macaq.ind)]

##################

#model.matrix(~Species+CellType+Sex+Age_Class+Conversion_rates+Species:CellType,pData(bs.PR.olig))
#SpeciesHuman SpeciesMacaque CellTypeOlig SpeciesHuman:CellTypeOlig
#DMLfit = DMLfit.multiFactor(bs.celltype.human,pData(bs.celltype.human), ~CellType+Sex+Age_Class+Conversion_rates)

DMLfit = DMLfit.multiFactor(bs.combine.filtered,pData(bs.combine.filtered), ~CellType+Species+Sex+Age_Class+Conversion_rates)
DMLtest = DMLtest.multiFactor(DMLfit, coef="CellTypeOlig")
#write.table(DMLtest,file=paste0(args[2],"_Celltype.txt"),sep="\t",row.names=F,quote=F)
pval_max <- DMLtest[DMLtest$pvals<0.005,][which.max(DMLtest[DMLtest$pvals<0.005,]$pvals),]
DMRtest <- callDMR(DMLtest, p.threshold=0.005,minCG=4)
DMRtest_filtered <- DMRtest[(abs(DMRtest$areaStat) / DMRtest$nCG) > abs(pval_max$stat),]
write.table(DMRtest,file=paste0(args[2],"_Celltype.DMR.fdrs.txt"),sep="\t",row.names=F,quote=F)
write.table(DMRtest_filtered,file=paste0(args[2],"_Celltype.DMR.fdrs.filtered.txt"),sep="\t",row.names=F,quote=F)

#DMLfit = DMLfit.multiFactor(bs.celltype.human,pData(bs.celltype.human), ~CellType+Sex+Age_Class+Conversion_rates)
#DMLtest = DMLtest.multiFactor(DMLfit, coef="CellTypeOlig")
#write.table(DMLtest,file=paste0(args[2],"_Celltype_human.txt"),sep="\t",row.names=F,quote=F)

#DMLfit = DMLfit.multiFactor(bs.celltype.chimp,pData(bs.celltype.chimp), ~CellType+Sex+Age_Class+Conversion_rates)
#DMLtest = DMLtest.multiFactor(DMLfit, coef="CellTypeOlig")
#write.table(DMLtest,file=paste0(args[2],"_Celltype_chimp.txt"),sep="\t",row.names=F,quote=F)

#DMLfit = DMLfit.multiFactor(bs.celltype.macaq,pData(bs.celltype.macaq), ~CellType+Sex+Age_Class+Conversion_rates)
#DMLtest = DMLtest.multiFactor(DMLfit, coef="CellTypeOlig")
#write.table(DMLtest,file=paste0(args[2],"_Celltype_macaq.txt"),sep="\t",row.names=F,quote=F)

