class Post < ActiveRecord::Base
  attr_accessible :mobileNumber, :simNumber, :smsText, :smsTimeStamp
end
