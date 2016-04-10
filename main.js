//get the average return
var averageReturn = function(dataset){
	var sum = 0;
	for (var i = dataset.length-1; i > 0; i--) {
		var closeprice = Number(dataset[i].Close);
		var closepriceSecondDay = Number(dataset[i-1].Close);
		var actualReturn = (closepriceSecondDay - closeprice)/ closeprice;
		sum += actualReturn;
	}
	// console.log(sum);
	var averagereturn = sum / (dataset.length);
	return averagereturn;
};

var averageVolatility = function(averagereturn, dataset){
	var sum = 0;
	for (var i = dataset.length-1; i > 0; i--) {
		var closeprice = Number(dataset[i].Close);
		var closepriceSecondDay = Number(dataset[i-1].Close);
		var actualReturn = (closepriceSecondDay - closeprice)/ closeprice;
		var deviation = Math.pow(actualReturn-averagereturn, 2);
		// console.log(deviation);
		sum += deviation;
	}
	var variance = sum / (dataset.length);
	var sd = Math.sqrt(variance);
	return sd;
};

var dataset;


function loadData(dataname){
	d3.csv(dataname, function(error, data) {
		if (error) {
			console.log('error');
		} else {
			dataset = data;
			console.log(dataname);
			var averageReturnOfCompany = averageReturn(dataset);
			console.log("average return:");
			console.log(averageReturnOfCompany);
			var averageSD = averageVolatility(averageReturnOfCompany, dataset);
			console.log("average volatility:");
			console.log(averageSD);
		}
	});
}

mydatalist = ['baba.csv', 'aci.csv', 'ibm.csv', 'ogzpy.csv', 'panw.csv', 'ptr.csv', 'table.csv', 'xom.csv'];
$('document').ready(function(){
	for (var i = 0; i < mydatalist.length; i++) {
		loadData(mydatalist[i]);
	}
});