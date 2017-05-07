Section = function(sec_name, sec_desc){
	this.sectionHeading = ko.observable(sec_name);
	this.head_desc = ko.observable(sec_desc);
	this.elementList = ko.observableArray([]);

	this.addElement = function(){
		this.elementList.push({"label": "A", "linkHead": "", "linkUrl":"", "linkComment":""})
	}.bind(this)

	this.removeElement = function(dynamicField){
		this.elementList.remove(dynamicField)
	}.bind(this)

    // this.setHeading = function(sec_name){
    //     this.sectionHeading = sec_name
    // }
};

var Element = function(){
	this.label =  ko.observable("Variable");
	this.linkHead = ko.observable("");
	this.linkUrl = ko.observable("");
	this.linkComment = ko.observable(""); 
}

// Section.prototype.addElementM = function(){
// 	this.elementList.push({"label": "Change", "linkHead": "", "linkUrl":"", "linkComment":""})
// }

function fieldModel(){
    var self = this;

    self.sectionList = ko.observableArray();
    //self.sectionList.push(new Section());

    self.removeSection = function(dynamicField){
    	self.sectionList.remove(dynamicField);
    	console.log(sectionList());
    }

    self.addSection = function(){
    	self.sectionList.push(new Section());
    	console.log(sectionList());	
    }


    self.addNewSection = function(formElement){
        var sec_name = document.getElementById("sec_name").value
        var sec_desc = document.getElementById("sec_desc").value

        self.sectionList.push(new Section(sec_name,sec_desc));

        document.getElementById("sec_name").value = ""
        document.getElementById("sec_desc").value = ""

        console.log(sectionList()); 


    }

    // self.addElement = function(){

    // 	//self.addElementM()
    // 	//elementList.push({"label": "Change", "linkHead": "", "linkUrl":"", "linkComment":""})
    // }

	// self.elementList = ko.observableArray();
	// self.elementList.push(new Element());

    // self.removeElement = function(dynamicField){
    //     self.elementList.remove(dynamicField);
    //     console.log(elementList());
    // }
 
    // self.addElement = function() {
    //     self.elementList.push(new Element())
    //     console.log(elementList())
    // }


}

ko.applyBindings(fieldModel);

//auto adjust height of textarea
function textAreaAdjust(o) {
  o.style.height = "1px";
  o.style.height = (o.scrollHeight)+"px";
}
//convert model to JSON
//jsonData = ko.toJSON(sectionList)