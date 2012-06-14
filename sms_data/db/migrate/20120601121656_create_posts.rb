class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.string, :mobileNumber
      t.string, :smsTimeStamp
      t.text, :smsText
      t.string :simNumber

      t.timestamps
    end
  end
end
