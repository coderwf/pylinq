# Generated from SqlParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from parser.SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#root.
    def enterRoot(self, ctx:SqlParser.RootContext):
        pass

    # Exit a parse tree produced by SqlParser#root.
    def exitRoot(self, ctx:SqlParser.RootContext):
        pass


    # Enter a parse tree produced by SqlParser#sqlStatements.
    def enterSqlStatements(self, ctx:SqlParser.SqlStatementsContext):
        pass

    # Exit a parse tree produced by SqlParser#sqlStatements.
    def exitSqlStatements(self, ctx:SqlParser.SqlStatementsContext):
        pass


    # Enter a parse tree produced by SqlParser#sqlStatement.
    def enterSqlStatement(self, ctx:SqlParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#sqlStatement.
    def exitSqlStatement(self, ctx:SqlParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#emptyStatement.
    def enterEmptyStatement(self, ctx:SqlParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#emptyStatement.
    def exitEmptyStatement(self, ctx:SqlParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#dmlStatement.
    def enterDmlStatement(self, ctx:SqlParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#dmlStatement.
    def exitDmlStatement(self, ctx:SqlParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#timestampValue.
    def enterTimestampValue(self, ctx:SqlParser.TimestampValueContext):
        pass

    # Exit a parse tree produced by SqlParser#timestampValue.
    def exitTimestampValue(self, ctx:SqlParser.TimestampValueContext):
        pass


    # Enter a parse tree produced by SqlParser#intervalExpr.
    def enterIntervalExpr(self, ctx:SqlParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by SqlParser#intervalExpr.
    def exitIntervalExpr(self, ctx:SqlParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by SqlParser#intervalType.
    def enterIntervalType(self, ctx:SqlParser.IntervalTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#intervalType.
    def exitIntervalType(self, ctx:SqlParser.IntervalTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#functionParameter.
    def enterFunctionParameter(self, ctx:SqlParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by SqlParser#functionParameter.
    def exitFunctionParameter(self, ctx:SqlParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by SqlParser#simpleSelect.
    def enterSimpleSelect(self, ctx:SqlParser.SimpleSelectContext):
        pass

    # Exit a parse tree produced by SqlParser#simpleSelect.
    def exitSimpleSelect(self, ctx:SqlParser.SimpleSelectContext):
        pass


    # Enter a parse tree produced by SqlParser#parenthesisSelect.
    def enterParenthesisSelect(self, ctx:SqlParser.ParenthesisSelectContext):
        pass

    # Exit a parse tree produced by SqlParser#parenthesisSelect.
    def exitParenthesisSelect(self, ctx:SqlParser.ParenthesisSelectContext):
        pass


    # Enter a parse tree produced by SqlParser#orderByClause.
    def enterOrderByClause(self, ctx:SqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#orderByClause.
    def exitOrderByClause(self, ctx:SqlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#orderByExpression.
    def enterOrderByExpression(self, ctx:SqlParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#orderByExpression.
    def exitOrderByExpression(self, ctx:SqlParser.OrderByExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#tableSources.
    def enterTableSources(self, ctx:SqlParser.TableSourcesContext):
        pass

    # Exit a parse tree produced by SqlParser#tableSources.
    def exitTableSources(self, ctx:SqlParser.TableSourcesContext):
        pass


    # Enter a parse tree produced by SqlParser#tableSourceBase.
    def enterTableSourceBase(self, ctx:SqlParser.TableSourceBaseContext):
        pass

    # Exit a parse tree produced by SqlParser#tableSourceBase.
    def exitTableSourceBase(self, ctx:SqlParser.TableSourceBaseContext):
        pass


    # Enter a parse tree produced by SqlParser#tableSourceNested.
    def enterTableSourceNested(self, ctx:SqlParser.TableSourceNestedContext):
        pass

    # Exit a parse tree produced by SqlParser#tableSourceNested.
    def exitTableSourceNested(self, ctx:SqlParser.TableSourceNestedContext):
        pass


    # Enter a parse tree produced by SqlParser#atomTableItem.
    def enterAtomTableItem(self, ctx:SqlParser.AtomTableItemContext):
        pass

    # Exit a parse tree produced by SqlParser#atomTableItem.
    def exitAtomTableItem(self, ctx:SqlParser.AtomTableItemContext):
        pass


    # Enter a parse tree produced by SqlParser#subqueryTableItem.
    def enterSubqueryTableItem(self, ctx:SqlParser.SubqueryTableItemContext):
        pass

    # Exit a parse tree produced by SqlParser#subqueryTableItem.
    def exitSubqueryTableItem(self, ctx:SqlParser.SubqueryTableItemContext):
        pass


    # Enter a parse tree produced by SqlParser#innerJoin.
    def enterInnerJoin(self, ctx:SqlParser.InnerJoinContext):
        pass

    # Exit a parse tree produced by SqlParser#innerJoin.
    def exitInnerJoin(self, ctx:SqlParser.InnerJoinContext):
        pass


    # Enter a parse tree produced by SqlParser#straightJoin.
    def enterStraightJoin(self, ctx:SqlParser.StraightJoinContext):
        pass

    # Exit a parse tree produced by SqlParser#straightJoin.
    def exitStraightJoin(self, ctx:SqlParser.StraightJoinContext):
        pass


    # Enter a parse tree produced by SqlParser#outerJoin.
    def enterOuterJoin(self, ctx:SqlParser.OuterJoinContext):
        pass

    # Exit a parse tree produced by SqlParser#outerJoin.
    def exitOuterJoin(self, ctx:SqlParser.OuterJoinContext):
        pass


    # Enter a parse tree produced by SqlParser#queryExpression.
    def enterQueryExpression(self, ctx:SqlParser.QueryExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#queryExpression.
    def exitQueryExpression(self, ctx:SqlParser.QueryExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#querySpecification.
    def enterQuerySpecification(self, ctx:SqlParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SqlParser#querySpecification.
    def exitQuerySpecification(self, ctx:SqlParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SqlParser#selectSpec.
    def enterSelectSpec(self, ctx:SqlParser.SelectSpecContext):
        pass

    # Exit a parse tree produced by SqlParser#selectSpec.
    def exitSelectSpec(self, ctx:SqlParser.SelectSpecContext):
        pass


    # Enter a parse tree produced by SqlParser#selectElements.
    def enterSelectElements(self, ctx:SqlParser.SelectElementsContext):
        pass

    # Exit a parse tree produced by SqlParser#selectElements.
    def exitSelectElements(self, ctx:SqlParser.SelectElementsContext):
        pass


    # Enter a parse tree produced by SqlParser#selectStarElement.
    def enterSelectStarElement(self, ctx:SqlParser.SelectStarElementContext):
        pass

    # Exit a parse tree produced by SqlParser#selectStarElement.
    def exitSelectStarElement(self, ctx:SqlParser.SelectStarElementContext):
        pass


    # Enter a parse tree produced by SqlParser#selectColumnElement.
    def enterSelectColumnElement(self, ctx:SqlParser.SelectColumnElementContext):
        pass

    # Exit a parse tree produced by SqlParser#selectColumnElement.
    def exitSelectColumnElement(self, ctx:SqlParser.SelectColumnElementContext):
        pass


    # Enter a parse tree produced by SqlParser#selectFunctionElement.
    def enterSelectFunctionElement(self, ctx:SqlParser.SelectFunctionElementContext):
        pass

    # Exit a parse tree produced by SqlParser#selectFunctionElement.
    def exitSelectFunctionElement(self, ctx:SqlParser.SelectFunctionElementContext):
        pass


    # Enter a parse tree produced by SqlParser#selectExpressionElement.
    def enterSelectExpressionElement(self, ctx:SqlParser.SelectExpressionElementContext):
        pass

    # Exit a parse tree produced by SqlParser#selectExpressionElement.
    def exitSelectExpressionElement(self, ctx:SqlParser.SelectExpressionElementContext):
        pass


    # Enter a parse tree produced by SqlParser#fromClause.
    def enterFromClause(self, ctx:SqlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#fromClause.
    def exitFromClause(self, ctx:SqlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#groupByItem.
    def enterGroupByItem(self, ctx:SqlParser.GroupByItemContext):
        pass

    # Exit a parse tree produced by SqlParser#groupByItem.
    def exitGroupByItem(self, ctx:SqlParser.GroupByItemContext):
        pass


    # Enter a parse tree produced by SqlParser#limitClause.
    def enterLimitClause(self, ctx:SqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#limitClause.
    def exitLimitClause(self, ctx:SqlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#fullId.
    def enterFullId(self, ctx:SqlParser.FullIdContext):
        pass

    # Exit a parse tree produced by SqlParser#fullId.
    def exitFullId(self, ctx:SqlParser.FullIdContext):
        pass


    # Enter a parse tree produced by SqlParser#tableName.
    def enterTableName(self, ctx:SqlParser.TableNameContext):
        pass

    # Exit a parse tree produced by SqlParser#tableName.
    def exitTableName(self, ctx:SqlParser.TableNameContext):
        pass


    # Enter a parse tree produced by SqlParser#fullColumnName.
    def enterFullColumnName(self, ctx:SqlParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by SqlParser#fullColumnName.
    def exitFullColumnName(self, ctx:SqlParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by SqlParser#mysqlVariable.
    def enterMysqlVariable(self, ctx:SqlParser.MysqlVariableContext):
        pass

    # Exit a parse tree produced by SqlParser#mysqlVariable.
    def exitMysqlVariable(self, ctx:SqlParser.MysqlVariableContext):
        pass


    # Enter a parse tree produced by SqlParser#uid.
    def enterUid(self, ctx:SqlParser.UidContext):
        pass

    # Exit a parse tree produced by SqlParser#uid.
    def exitUid(self, ctx:SqlParser.UidContext):
        pass


    # Enter a parse tree produced by SqlParser#simpleId.
    def enterSimpleId(self, ctx:SqlParser.SimpleIdContext):
        pass

    # Exit a parse tree produced by SqlParser#simpleId.
    def exitSimpleId(self, ctx:SqlParser.SimpleIdContext):
        pass


    # Enter a parse tree produced by SqlParser#dottedId.
    def enterDottedId(self, ctx:SqlParser.DottedIdContext):
        pass

    # Exit a parse tree produced by SqlParser#dottedId.
    def exitDottedId(self, ctx:SqlParser.DottedIdContext):
        pass


    # Enter a parse tree produced by SqlParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SqlParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SqlParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#stringLiteral.
    def enterStringLiteral(self, ctx:SqlParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#stringLiteral.
    def exitStringLiteral(self, ctx:SqlParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SqlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SqlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#hexadecimalLiteral.
    def enterHexadecimalLiteral(self, ctx:SqlParser.HexadecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#hexadecimalLiteral.
    def exitHexadecimalLiteral(self, ctx:SqlParser.HexadecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#nullNotnull.
    def enterNullNotnull(self, ctx:SqlParser.NullNotnullContext):
        pass

    # Exit a parse tree produced by SqlParser#nullNotnull.
    def exitNullNotnull(self, ctx:SqlParser.NullNotnullContext):
        pass


    # Enter a parse tree produced by SqlParser#constant.
    def enterConstant(self, ctx:SqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by SqlParser#constant.
    def exitConstant(self, ctx:SqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by SqlParser#simpleDataType.
    def enterSimpleDataType(self, ctx:SqlParser.SimpleDataTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#simpleDataType.
    def exitSimpleDataType(self, ctx:SqlParser.SimpleDataTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#spatialDataType.
    def enterSpatialDataType(self, ctx:SqlParser.SpatialDataTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#spatialDataType.
    def exitSpatialDataType(self, ctx:SqlParser.SpatialDataTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#convertedDataType.
    def enterConvertedDataType(self, ctx:SqlParser.ConvertedDataTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#convertedDataType.
    def exitConvertedDataType(self, ctx:SqlParser.ConvertedDataTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#uidList.
    def enterUidList(self, ctx:SqlParser.UidListContext):
        pass

    # Exit a parse tree produced by SqlParser#uidList.
    def exitUidList(self, ctx:SqlParser.UidListContext):
        pass


    # Enter a parse tree produced by SqlParser#tables.
    def enterTables(self, ctx:SqlParser.TablesContext):
        pass

    # Exit a parse tree produced by SqlParser#tables.
    def exitTables(self, ctx:SqlParser.TablesContext):
        pass


    # Enter a parse tree produced by SqlParser#expressions.
    def enterExpressions(self, ctx:SqlParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by SqlParser#expressions.
    def exitExpressions(self, ctx:SqlParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by SqlParser#expressionsWithDefaults.
    def enterExpressionsWithDefaults(self, ctx:SqlParser.ExpressionsWithDefaultsContext):
        pass

    # Exit a parse tree produced by SqlParser#expressionsWithDefaults.
    def exitExpressionsWithDefaults(self, ctx:SqlParser.ExpressionsWithDefaultsContext):
        pass


    # Enter a parse tree produced by SqlParser#constants.
    def enterConstants(self, ctx:SqlParser.ConstantsContext):
        pass

    # Exit a parse tree produced by SqlParser#constants.
    def exitConstants(self, ctx:SqlParser.ConstantsContext):
        pass


    # Enter a parse tree produced by SqlParser#simpleStrings.
    def enterSimpleStrings(self, ctx:SqlParser.SimpleStringsContext):
        pass

    # Exit a parse tree produced by SqlParser#simpleStrings.
    def exitSimpleStrings(self, ctx:SqlParser.SimpleStringsContext):
        pass


    # Enter a parse tree produced by SqlParser#userVariables.
    def enterUserVariables(self, ctx:SqlParser.UserVariablesContext):
        pass

    # Exit a parse tree produced by SqlParser#userVariables.
    def exitUserVariables(self, ctx:SqlParser.UserVariablesContext):
        pass


    # Enter a parse tree produced by SqlParser#defaultValue.
    def enterDefaultValue(self, ctx:SqlParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by SqlParser#defaultValue.
    def exitDefaultValue(self, ctx:SqlParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by SqlParser#currentTimestamp.
    def enterCurrentTimestamp(self, ctx:SqlParser.CurrentTimestampContext):
        pass

    # Exit a parse tree produced by SqlParser#currentTimestamp.
    def exitCurrentTimestamp(self, ctx:SqlParser.CurrentTimestampContext):
        pass


    # Enter a parse tree produced by SqlParser#expressionOrDefault.
    def enterExpressionOrDefault(self, ctx:SqlParser.ExpressionOrDefaultContext):
        pass

    # Exit a parse tree produced by SqlParser#expressionOrDefault.
    def exitExpressionOrDefault(self, ctx:SqlParser.ExpressionOrDefaultContext):
        pass


    # Enter a parse tree produced by SqlParser#ifExists.
    def enterIfExists(self, ctx:SqlParser.IfExistsContext):
        pass

    # Exit a parse tree produced by SqlParser#ifExists.
    def exitIfExists(self, ctx:SqlParser.IfExistsContext):
        pass


    # Enter a parse tree produced by SqlParser#ifNotExists.
    def enterIfNotExists(self, ctx:SqlParser.IfNotExistsContext):
        pass

    # Exit a parse tree produced by SqlParser#ifNotExists.
    def exitIfNotExists(self, ctx:SqlParser.IfNotExistsContext):
        pass


    # Enter a parse tree produced by SqlParser#specificFunctionCall.
    def enterSpecificFunctionCall(self, ctx:SqlParser.SpecificFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#specificFunctionCall.
    def exitSpecificFunctionCall(self, ctx:SqlParser.SpecificFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#aggregateFunctionCall.
    def enterAggregateFunctionCall(self, ctx:SqlParser.AggregateFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#aggregateFunctionCall.
    def exitAggregateFunctionCall(self, ctx:SqlParser.AggregateFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#scalarFunctionCall.
    def enterScalarFunctionCall(self, ctx:SqlParser.ScalarFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#scalarFunctionCall.
    def exitScalarFunctionCall(self, ctx:SqlParser.ScalarFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#udfFunctionCall.
    def enterUdfFunctionCall(self, ctx:SqlParser.UdfFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#udfFunctionCall.
    def exitUdfFunctionCall(self, ctx:SqlParser.UdfFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#simpleFunctionCall.
    def enterSimpleFunctionCall(self, ctx:SqlParser.SimpleFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#simpleFunctionCall.
    def exitSimpleFunctionCall(self, ctx:SqlParser.SimpleFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#dataTypeFunctionCall.
    def enterDataTypeFunctionCall(self, ctx:SqlParser.DataTypeFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#dataTypeFunctionCall.
    def exitDataTypeFunctionCall(self, ctx:SqlParser.DataTypeFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#valuesFunctionCall.
    def enterValuesFunctionCall(self, ctx:SqlParser.ValuesFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#valuesFunctionCall.
    def exitValuesFunctionCall(self, ctx:SqlParser.ValuesFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#caseFunctionCall.
    def enterCaseFunctionCall(self, ctx:SqlParser.CaseFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#caseFunctionCall.
    def exitCaseFunctionCall(self, ctx:SqlParser.CaseFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#charFunctionCall.
    def enterCharFunctionCall(self, ctx:SqlParser.CharFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#charFunctionCall.
    def exitCharFunctionCall(self, ctx:SqlParser.CharFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#positionFunctionCall.
    def enterPositionFunctionCall(self, ctx:SqlParser.PositionFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#positionFunctionCall.
    def exitPositionFunctionCall(self, ctx:SqlParser.PositionFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#substrFunctionCall.
    def enterSubstrFunctionCall(self, ctx:SqlParser.SubstrFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#substrFunctionCall.
    def exitSubstrFunctionCall(self, ctx:SqlParser.SubstrFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#trimFunctionCall.
    def enterTrimFunctionCall(self, ctx:SqlParser.TrimFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#trimFunctionCall.
    def exitTrimFunctionCall(self, ctx:SqlParser.TrimFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#weightFunctionCall.
    def enterWeightFunctionCall(self, ctx:SqlParser.WeightFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#weightFunctionCall.
    def exitWeightFunctionCall(self, ctx:SqlParser.WeightFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#extractFunctionCall.
    def enterExtractFunctionCall(self, ctx:SqlParser.ExtractFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#extractFunctionCall.
    def exitExtractFunctionCall(self, ctx:SqlParser.ExtractFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#getFormatFunctionCall.
    def enterGetFormatFunctionCall(self, ctx:SqlParser.GetFormatFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#getFormatFunctionCall.
    def exitGetFormatFunctionCall(self, ctx:SqlParser.GetFormatFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#caseFuncAlternative.
    def enterCaseFuncAlternative(self, ctx:SqlParser.CaseFuncAlternativeContext):
        pass

    # Exit a parse tree produced by SqlParser#caseFuncAlternative.
    def exitCaseFuncAlternative(self, ctx:SqlParser.CaseFuncAlternativeContext):
        pass


    # Enter a parse tree produced by SqlParser#aggregateWindowedFunction.
    def enterAggregateWindowedFunction(self, ctx:SqlParser.AggregateWindowedFunctionContext):
        pass

    # Exit a parse tree produced by SqlParser#aggregateWindowedFunction.
    def exitAggregateWindowedFunction(self, ctx:SqlParser.AggregateWindowedFunctionContext):
        pass


    # Enter a parse tree produced by SqlParser#scalarFunctionName.
    def enterScalarFunctionName(self, ctx:SqlParser.ScalarFunctionNameContext):
        pass

    # Exit a parse tree produced by SqlParser#scalarFunctionName.
    def exitScalarFunctionName(self, ctx:SqlParser.ScalarFunctionNameContext):
        pass


    # Enter a parse tree produced by SqlParser#functionArgs.
    def enterFunctionArgs(self, ctx:SqlParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by SqlParser#functionArgs.
    def exitFunctionArgs(self, ctx:SqlParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by SqlParser#functionArg.
    def enterFunctionArg(self, ctx:SqlParser.FunctionArgContext):
        pass

    # Exit a parse tree produced by SqlParser#functionArg.
    def exitFunctionArg(self, ctx:SqlParser.FunctionArgContext):
        pass


    # Enter a parse tree produced by SqlParser#isExpression.
    def enterIsExpression(self, ctx:SqlParser.IsExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#isExpression.
    def exitIsExpression(self, ctx:SqlParser.IsExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#notExpression.
    def enterNotExpression(self, ctx:SqlParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#notExpression.
    def exitNotExpression(self, ctx:SqlParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#logicalExpression.
    def enterLogicalExpression(self, ctx:SqlParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#logicalExpression.
    def exitLogicalExpression(self, ctx:SqlParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#predicateExpression.
    def enterPredicateExpression(self, ctx:SqlParser.PredicateExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#predicateExpression.
    def exitPredicateExpression(self, ctx:SqlParser.PredicateExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#soundsLikePredicate.
    def enterSoundsLikePredicate(self, ctx:SqlParser.SoundsLikePredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#soundsLikePredicate.
    def exitSoundsLikePredicate(self, ctx:SqlParser.SoundsLikePredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#expressionAtomPredicate.
    def enterExpressionAtomPredicate(self, ctx:SqlParser.ExpressionAtomPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#expressionAtomPredicate.
    def exitExpressionAtomPredicate(self, ctx:SqlParser.ExpressionAtomPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#inPredicate.
    def enterInPredicate(self, ctx:SqlParser.InPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#inPredicate.
    def exitInPredicate(self, ctx:SqlParser.InPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#subqueryComparasionPredicate.
    def enterSubqueryComparasionPredicate(self, ctx:SqlParser.SubqueryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#subqueryComparasionPredicate.
    def exitSubqueryComparasionPredicate(self, ctx:SqlParser.SubqueryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#binaryComparationPredicate.
    def enterBinaryComparationPredicate(self, ctx:SqlParser.BinaryComparationPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#binaryComparationPredicate.
    def exitBinaryComparationPredicate(self, ctx:SqlParser.BinaryComparationPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx:SqlParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx:SqlParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#isNullPredicate.
    def enterIsNullPredicate(self, ctx:SqlParser.IsNullPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#isNullPredicate.
    def exitIsNullPredicate(self, ctx:SqlParser.IsNullPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#likePredicate.
    def enterLikePredicate(self, ctx:SqlParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#likePredicate.
    def exitLikePredicate(self, ctx:SqlParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#regexpPredicate.
    def enterRegexpPredicate(self, ctx:SqlParser.RegexpPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#regexpPredicate.
    def exitRegexpPredicate(self, ctx:SqlParser.RegexpPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#unaryExpressionAtom.
    def enterUnaryExpressionAtom(self, ctx:SqlParser.UnaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#unaryExpressionAtom.
    def exitUnaryExpressionAtom(self, ctx:SqlParser.UnaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#subqueryExpressionAtom.
    def enterSubqueryExpressionAtom(self, ctx:SqlParser.SubqueryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#subqueryExpressionAtom.
    def exitSubqueryExpressionAtom(self, ctx:SqlParser.SubqueryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#constantExpressionAtom.
    def enterConstantExpressionAtom(self, ctx:SqlParser.ConstantExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#constantExpressionAtom.
    def exitConstantExpressionAtom(self, ctx:SqlParser.ConstantExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#functionCallExpressionAtom.
    def enterFunctionCallExpressionAtom(self, ctx:SqlParser.FunctionCallExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#functionCallExpressionAtom.
    def exitFunctionCallExpressionAtom(self, ctx:SqlParser.FunctionCallExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#binaryExpressionAtom.
    def enterBinaryExpressionAtom(self, ctx:SqlParser.BinaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#binaryExpressionAtom.
    def exitBinaryExpressionAtom(self, ctx:SqlParser.BinaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#fullColumnNameExpressionAtom.
    def enterFullColumnNameExpressionAtom(self, ctx:SqlParser.FullColumnNameExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#fullColumnNameExpressionAtom.
    def exitFullColumnNameExpressionAtom(self, ctx:SqlParser.FullColumnNameExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#bitExpressionAtom.
    def enterBitExpressionAtom(self, ctx:SqlParser.BitExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#bitExpressionAtom.
    def exitBitExpressionAtom(self, ctx:SqlParser.BitExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#nestedExpressionAtom.
    def enterNestedExpressionAtom(self, ctx:SqlParser.NestedExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#nestedExpressionAtom.
    def exitNestedExpressionAtom(self, ctx:SqlParser.NestedExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#mathExpressionAtom.
    def enterMathExpressionAtom(self, ctx:SqlParser.MathExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#mathExpressionAtom.
    def exitMathExpressionAtom(self, ctx:SqlParser.MathExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#existsExpressionAtom.
    def enterExistsExpressionAtom(self, ctx:SqlParser.ExistsExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#existsExpressionAtom.
    def exitExistsExpressionAtom(self, ctx:SqlParser.ExistsExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#intervalExpressionAtom.
    def enterIntervalExpressionAtom(self, ctx:SqlParser.IntervalExpressionAtomContext):
        pass

    # Exit a parse tree produced by SqlParser#intervalExpressionAtom.
    def exitIntervalExpressionAtom(self, ctx:SqlParser.IntervalExpressionAtomContext):
        pass


    # Enter a parse tree produced by SqlParser#unaryOperator.
    def enterUnaryOperator(self, ctx:SqlParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by SqlParser#unaryOperator.
    def exitUnaryOperator(self, ctx:SqlParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by SqlParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SqlParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SqlParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SqlParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SqlParser#logicalOperator.
    def enterLogicalOperator(self, ctx:SqlParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by SqlParser#logicalOperator.
    def exitLogicalOperator(self, ctx:SqlParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by SqlParser#bitOperator.
    def enterBitOperator(self, ctx:SqlParser.BitOperatorContext):
        pass

    # Exit a parse tree produced by SqlParser#bitOperator.
    def exitBitOperator(self, ctx:SqlParser.BitOperatorContext):
        pass


    # Enter a parse tree produced by SqlParser#mathOperator.
    def enterMathOperator(self, ctx:SqlParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by SqlParser#mathOperator.
    def exitMathOperator(self, ctx:SqlParser.MathOperatorContext):
        pass


    # Enter a parse tree produced by SqlParser#intervalTypeBase.
    def enterIntervalTypeBase(self, ctx:SqlParser.IntervalTypeBaseContext):
        pass

    # Exit a parse tree produced by SqlParser#intervalTypeBase.
    def exitIntervalTypeBase(self, ctx:SqlParser.IntervalTypeBaseContext):
        pass


    # Enter a parse tree produced by SqlParser#dataTypeBase.
    def enterDataTypeBase(self, ctx:SqlParser.DataTypeBaseContext):
        pass

    # Exit a parse tree produced by SqlParser#dataTypeBase.
    def exitDataTypeBase(self, ctx:SqlParser.DataTypeBaseContext):
        pass


    # Enter a parse tree produced by SqlParser#keywordsCanBeId.
    def enterKeywordsCanBeId(self, ctx:SqlParser.KeywordsCanBeIdContext):
        pass

    # Exit a parse tree produced by SqlParser#keywordsCanBeId.
    def exitKeywordsCanBeId(self, ctx:SqlParser.KeywordsCanBeIdContext):
        pass


    # Enter a parse tree produced by SqlParser#functionNameBase.
    def enterFunctionNameBase(self, ctx:SqlParser.FunctionNameBaseContext):
        pass

    # Exit a parse tree produced by SqlParser#functionNameBase.
    def exitFunctionNameBase(self, ctx:SqlParser.FunctionNameBaseContext):
        pass


